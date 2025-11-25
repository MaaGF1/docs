#!/bin/bash

# ========================================================
# Script Name: gen_ref.sh
# Function: Scan all .md files in current directory and generate ref.md index by directory structure
# ========================================================

# Define output filename
OUTPUT_FILE="ref.md"

# Clear or create output file, and write main title
echo "# Index (Reference)" > "$OUTPUT_FILE"
echo "> Auto-generated at $(date "+%Y-%m-%d %H:%M:%S")" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# Define an array to store previous loop's directory path parts
# Used to compare if path has changed
declare -a prev_parts=()

# 1. Find all .md files in current directory
# 2. Exclude output file itself (ref.md) to prevent infinite loop or self-reference
# 3. Sort to ensure files in same directory are grouped together
find . -type f -name "*.md" ! -name "$OUTPUT_FILE" | sort | while read -r filepath; do
    
    # Get file's directory path (e.g.: ./doc/tutorial/base)
    dir_path=$(dirname "$filepath")
    # Get filename (e.g.: 01_luffberry_chess.md)
    filename=$(basename "$filepath")
    
    # Remove leading "./" from path for processing (becomes doc/tutorial/base)
    # If file is in root directory, clean_dir_path is empty
    if [ "$dir_path" == "." ]; then
        clean_dir_path=""
    else
        clean_dir_path="${dir_path#./}"
    fi

    # Split path by '/' into array
    # IFS='/' defines the delimiter
    IFS='/' read -r -a curr_parts <<< "$clean_dir_path"

    # Flag to mark if path change is detected
    path_changed=false

    # Iterate through each level of current path
    for ((i=0; i<${#curr_parts[@]}; i++)); do
        curr_part="${curr_parts[$i]}"
        prev_part="${prev_parts[$i]}"

        # If current level differs from previous, or if higher levels have already changed
        if [[ "$path_changed" == true ]] || [[ "$curr_part" != "$prev_part" ]]; then
            path_changed=true
            
            # Calculate heading level.
            # Array index starts from 0, doc is level 0.
            # We can make doc correspond to level-1 heading #, or level-2 ##.
            # Here we set: level 0 (doc) = #, level 1 = ##, and so on.
            level=$((i + 1))
            
            # Generate corresponding number of '#'
            hashes=$(printf "%0.s#" $(seq 1 $level))
            
            # Write heading to file
            echo -e "\n$hashes $curr_part\n" >> "$OUTPUT_FILE"
        fi
    done

    # Write file link
    # Format: - [filename](relative_path)
    echo "- [$filename]($filepath)" >> "$OUTPUT_FILE"

    # Update prev_parts to current path for next loop comparison
    prev_parts=("${curr_parts[@]}")

done

echo "Generation completed! Please check $OUTPUT_FILE"