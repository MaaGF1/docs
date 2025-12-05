import os
import sys
import json
import subprocess
import google.generativeai as genai
from github import Github, Auth

# --- Config ---
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
REPO_NAME = os.environ.get("REPO_NAME")
ISSUE_NUMBER = int(os.environ.get("ISSUE_NUMBER"))
PROMPT_CONTENT = os.environ.get("PROMPT_CONTENT", "")

# 定义触发关键词列表
TRIGGERS = ["/gemini", "/丹德莱"]

def setup_gemini():
    genai.configure(api_key=GEMINI_API_KEY)
    return genai.GenerativeModel('gemini-2.5-flash')

def get_file_structure(root_dir="."):
    """获取文件结构，忽略无关目录"""
    file_tree = []
    exclude_dirs = {'.git', '.github', '__pycache__', 'site', 'venv', 'node_modules'}
    
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in files:
            if file.endswith(('.md', '.yml', '.py', '.css', '.txt')):
                path = os.path.join(root, file)
                file_tree.append(path)
    return "\n".join(file_tree)

def run_git_cmd(cmd):
    subprocess.run(cmd, shell=True, check=True)

def generate_dandelion_response(pr_url, ai_comment):
    """生成丹德莱风格的回复"""
    return f"""
指挥官，我是丹德莱。系统已响应您的请求。

---

**▌ 思维链分析 (Neural Cloud Analysis)**

{ai_comment}

---

**▌ 执行结果 (Execution Report)**

相关修改已封装至独立的子进程分支。
🔗 **Pull Request**: {pr_url}

请核查。如果一切正常，请批准合并。
"""

def main():
    # 1. 检查触发词
    if not PROMPT_CONTENT:
        print("Content is empty. Skipping.")
        sys.exit(0)

    active_trigger = None
    for trigger in TRIGGERS:
        if trigger in PROMPT_CONTENT:
            active_trigger = trigger
            break
    
    if not active_trigger:
        print(f"No triggers found in content. Expected one of: {TRIGGERS}")
        sys.exit(0)

    print(f"检测到触发词: {active_trigger}")

    # 2. 准备上下文
    print("正在分析项目结构...")
    file_tree = get_file_structure()
    
    # 移除触发词，提取真实需求
    user_request = PROMPT_CONTENT.replace(active_trigger, "").strip()
    
    # 3. 构建 Prompt
    # 关键修改：要求返回包含 comment 和 changes 的对象结构
    system_prompt = f"""
    你是一个专业的文档工程师，正在维护 `MaaGF1/docs` 项目（基于 MkDocs）。
    
    ## 一、项目结构
    {file_tree}
    
    ## 二、用户需求
    {user_request}
    
    ## 三、输出要求 (CRITICAL)
    请根据需求生成修改内容。**必须**返回且仅返回一个纯 JSON 对象（Object），包含两个字段：
    1. `comment`: (String) 简要描述你做了什么修改，以及你的思考逻辑。请用中文回答。
    2. `changes`: (List) 文件修改列表。

    JSON 格式示例：
    {{
        "comment": "检测到用户需要新增FAQ，我已在 docs/faq.md 中添加了相关章节，并更新了...",
        "changes": [
            {{
                "path": "docs/tutorial/new_guide.md",
                "content": "# 新文档标题\\n\\n内容..."
            }}
        ]
    }}

    ## 四、约束条件
    1. Markdown 内容要丰富、格式正确。
    2. **绝对不要**修改 `mkdocs.yml`，用户会自己处理。
    3. 不要输出 Markdown 代码块标记（如 ```json），只输出纯文本 JSON。
    """

    # 4. 调用 Gemini
    print("正在呼叫 Gemini...")
    model = setup_gemini()
    try:
        response = model.generate_content(system_prompt)
        response_text = response.text
        
        # 清理 Markdown 标记
        if response_text.startswith("```json"):
            response_text = response_text[7:]
        if response_text.startswith("```"):
            response_text = response_text[3:]
        if response_text.endswith("```"):
            response_text = response_text[:-3]
            
        data = json.loads(response_text)
        
        # 兼容性处理：防止 AI 偶尔还是返回了 List
        if isinstance(data, list):
            changes = data
            ai_comment = "系统未返回具体的思维链描述，但已执行文件修改。"
        else:
            changes = data.get("changes", [])
            ai_comment = data.get("comment", "操作已执行。")
            
    except Exception as e:
        print(f"Gemini 调用或 JSON 解析失败: {e}")
        try:
            print(f"原始返回: {response.text}")
        except:
            pass
        sys.exit(1)

    # 5. 应用更改
    print(f"收到 {len(changes)} 个文件变更请求。")
    print(f"AI 思考: {ai_comment}")
    
    # 配置 Git 用户
    run_git_cmd('git config --global user.name "Gemini Bot"')
    run_git_cmd('git config --global user.email "gemini-bot@actions.github.com"')
    
    # 创建新分支
    branch_name = f"ai/issue-{ISSUE_NUMBER}-{os.urandom(4).hex()}"
    run_git_cmd(f"git checkout -b {branch_name}")
    
    if not changes:
        print("AI 认为不需要修改任何文件。")
        # 这里可以选择直接退出，或者发个评论说不需要修改
        sys.exit(0)

    for change in changes:
        file_path = change['path']
        content = change['content']
        
        dir_name = os.path.dirname(file_path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"已写入: {file_path}")
        
        run_git_cmd(f'git add "{file_path}"')

    # 6. 提交并推送
    try:
        run_git_cmd(f'git commit -m "AI Auto-generated changes for Issue #{ISSUE_NUMBER}"')
        run_git_cmd(f"git push origin {branch_name}")
    except subprocess.CalledProcessError:
        print("没有检测到文件更改，跳过提交。")
        sys.exit(0)

    # 7. 创建 PR 并回复
    print("正在创建 Pull Request...")
    
    # 使用 Auth 解决 DeprecationWarning
    auth = Auth.Token(GITHUB_TOKEN)
    g = Github(auth=auth)
    
    repo = g.get_repo(REPO_NAME)
    issue = repo.get_issue(ISSUE_NUMBER)
    
    pr_body = f"""
    ## AI Auto-generated PR
    
    **Trigger:** `{active_trigger}`
    **Issue:** #{ISSUE_NUMBER}
    
    ### AI Analysis
    {ai_comment}
    """
    
    try:
        pr = repo.create_pull(
            title=f"AI: Fix for Issue #{ISSUE_NUMBER}",
            body=pr_body,
            head=branch_name,
            base="main"
        )
        
        # 生成丹德莱风格的回复
        dandelion_reply = generate_dandelion_response(pr.html_url, ai_comment)
        issue.create_comment(dandelion_reply)
        
        print(f"PR Created: {pr.html_url}")
        
    except Exception as e:
        print(f"创建 PR 失败: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()