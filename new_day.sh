#!/bin/bash

# Get the YEAR from the second argument, or fallback to the current year
YEAR="${2:-$(date +%Y)}"

# Function to pad the day number with leading zero if necessary
pad_day_number() {
  printf "%02d" "$1"
}

# Get the current day of the month if no argument is provided
if [ -z "$1" ]; then
  NON_PADDED_DAY=$(date +%-d)
else
  NON_PADDED_DAY="$1"
fi

DAY=$(pad_day_number "$NON_PADDED_DAY")

# Create directories for the day
mkdir -p "$YEAR/$DAY"

# Download input file from Advent of Code site if it doesn't exist
INPUT_FILE="$YEAR/$DAY/input"
if [ ! -f "$INPUT_FILE" ]; then
  if [ -z "$AOC_SESSION" ]; then
    echo "Error: AOC_SESSION environment variable is not set."
    exit 1
  fi

  curl -s -b "session=$AOC_SESSION" "https://adventofcode.com/$YEAR/day/$NON_PADDED_DAY/input" -o "$INPUT_FILE"
  if [ $? -ne 0 ]; then
    echo "Error: Failed to download input file."
    exit 1
  fi
fi

# Template for Python files
PYTHON_TEMPLATE="# Advent of Code $YEAR - Day $DAY – https://adventofcode.com/$YEAR/day/$NON_PADDED_DAY
f = open('./input', 'r')



if __name__ == '__main__':
    pass
"

# Create the Python files only if they don't already exist
PYTHON_FILE="$YEAR/$DAY/1.py"
if [ ! -f "$PYTHON_FILE" ]; then
  mkdir -p "$YEAR/$DAY"
  echo "$PYTHON_TEMPLATE" > "$PYTHON_FILE"
fi

# Create an empty __init__.py file for the day (if it doesn't exist)
INIT_FILE="$YEAR/$DAY/__init__.py"
if [ ! -f "$INIT_FILE" ]; then
  touch "$INIT_FILE"
fi

# Open IntelliJ IDEA with the current directory as the project root
idea .

# Give IntelliJ a moment to load the project, then open the Python file
sleep 2  # Add a small delay to ensure IntelliJ has time to open the project
idea --line 4 "$PYTHON_FILE"

if [ ! -f "$EXAMPLE_FILE" ]; then
  sleep 1
fi
# Open the browser on the problem statement
open "https://adventofcode.com/$YEAR/day/$NON_PADDED_DAY"

# Wait for user to copy the example input and write it to the example file
EXAMPLE_FILE="$YEAR/$DAY/example"
if [ ! -f "$EXAMPLE_FILE" ]; then
  echo "" | pbcopy
  INITIAL_CLIPBOARD_CONTENT=$(pbpaste)
  echo "Please copy the example input from the webpage. Waiting for new clipboard content..."
  while true; do
    EXAMPLE_INPUT=$(pbpaste)
    if [ "$EXAMPLE_INPUT" != "$INITIAL_CLIPBOARD_CONTENT" ] && [ -n "$EXAMPLE_INPUT" ]; then
      echo "$EXAMPLE_INPUT" > "$EXAMPLE_FILE"
      echo "Example input copied from clipboard to $EXAMPLE_FILE."
      break
    fi
    sleep 1
  done
fi

# Output success message
echo "Setup complete for Day $DAY. Files created:"
echo "- $YEAR/$DAY/example"
echo "- $YEAR/$DAY/input"
echo "- $YEAR/$DAY/1.py"
echo "- $YEAR/$DAY/__init__.py"
