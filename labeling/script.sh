#!/bin/bash

# Change to the directory where the script is located
cd "$(dirname "$0")"

while true; do
    # Select a random MP4 file from the 'videos' subdirectories
    FILES=( $(find videos -type f -name "*.mp4") )
    FILE_COUNT=${#FILES[@]}

    # If there are no files found, break the loop
    if [[ $FILE_COUNT -eq 0 ]]; then
        break
    fi

    RANDOM_INDEX=$(jot -r 1 0 $(($FILE_COUNT - 1)))
    FILE=${FILES[$RANDOM_INDEX]}

    # Move and rename the selected file
    mv "$FILE" "./vid.mp4"

    # Run the python script
    python3 video-labeling.py

    # Delete the renamed file
    rm -f ./vid.mp4
done

