#!/bin/bash

PIPPIN_TMP_FOLDER="/tmp/pippin"
PIPPIN_TMP_FILE="pippin_package_$PIPPIN_ITERATION_COUNT.txt"
PIPPIN_LIST="pippin_list.txt"
PIPPIN_FINAL_LIST="tmp_final_list.txt"
PIPPIN_PIP=${1:-"pip3"}
PIPPIN_ITERATION_COUNT=0

main() {
    cleanup # Ensure we have a fresh start (eg: keyboard interruption on last run)
    echo -e "Generating Pippin Report for \"$PIPPIN_PIP\"...\n"
    generate_pip_list
    breakdown_each_package
    cat "$PIPPIN_TMP_FOLDER/$PIPPIN_FINAL_LIST"
    cleanup
    echo "Pippin report complete! $PIPPIN_ITERATION_COUNT dependencies found for \"$PIPPIN_PIP\"."
}

generate_pip_list() {
    # Create and format the package list from Pip
    mkdir -p "$PIPPIN_TMP_FOLDER"
    "$PIPPIN_PIP" list --no-python-version-warning --disable-pip-version-check > "$PIPPIN_TMP_FOLDER/$PIPPIN_LIST"
    sed -i.bak '1,2d' "$PIPPIN_TMP_FOLDER/$PIPPIN_LIST" # Remove the headers from the pip package list
    sed -i.bak 's/ .*$//' "$PIPPIN_TMP_FOLDER/$PIPPIN_LIST" # Remove the version numbers from the pip package list
}

breakdown_each_package() {
    # Iterate through each package from the pip list and print data
    while read -r line; do
        "$PIPPIN_PIP" show --no-python-version-warning --disable-pip-version-check "$line" > "$PIPPIN_TMP_FOLDER/$PIPPIN_TMP_FILE"
        sed -i.bak '3,8d' "$PIPPIN_TMP_FOLDER/$PIPPIN_TMP_FILE" # Remove all rows but the "Name", "Requires", and "Required-by" fields
        cat "$PIPPIN_TMP_FOLDER/$PIPPIN_TMP_FILE" >> "$PIPPIN_TMP_FOLDER/$PIPPIN_FINAL_LIST"
        echo -e "" >> "$PIPPIN_TMP_FOLDER/$PIPPIN_FINAL_LIST"
        (( PIPPIN_ITERATION_COUNT+=1 ))
    done <"$PIPPIN_TMP_FOLDER/$PIPPIN_LIST"
}

cleanup() {
    # Remove the temporary files and folder used to generate the report
    rm -rf "$PIPPIN_TMP_FOLDER"
}

main
