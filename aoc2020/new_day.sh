#!/bin/bash

YEAR=2020

# Function to pad the day number with leading zero if necessary
pad_day_number() {
  printf "%02d" "$1"
}

# Get the current day of the month if no argument is provided
if [ -z "$1" ]; then
  NON_PADDED_DAY=$(date +%d)
else
  NON_PADDED_DAY="$1"
fi

DAY=$(pad_day_number "$NON_PADDED_DAY")

# Create directories and files
mkdir -p "input/day$DAY"

# Download input file from Advent of Code site if it doesn't exist
INPUT_FILE="input/day$DAY/input"
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

# Template for Rust file
RUST_TEMPLATE="// Advent of Code $YEAR - Day $DAY – https://adventofcode.com/$YEAR/day/$NON_PADDED_DAY/

use aoc2020::print_answers;

fn main() {
    print_answers(solve(include_str!(\"../../input/day$DAY/input\")));
}

fn solve(input: &str) -> (u32, u32) {
  let mut ans1 = 0;
  let mut ans2 = 0;

  (ans1, ans2)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_input_own() {
        let (part1_answer, part2_answer) = solve(include_str!(\"../../input/day$DAY/input\"));
        assert_eq!(part1_answer, 0);
        assert_eq!(part2_answer, 0);
    }

    #[test]
    fn test_input_example() {
        let (part1_answer, part2_answer) = solve(include_str!(\"../../input/day$DAY/example\"));
        assert_eq!(part1_answer, 0);
        assert_eq!(part2_answer, 0);
    }
}
"

# Create the Rust source file only if it doesn't already exist
RUST_FILE="src/bin/day$DAY.rs"
if [ ! -f "$RUST_FILE" ]; then
  mkdir -p "src/bin"
  echo "$RUST_TEMPLATE" > "$RUST_FILE"
fi

# Open RustRover on the Rust source file
open -a RustRover "$RUST_FILE"

if [ ! -f "$EXAMPLE_FILE" ]; then
  sleep 1
fi
# Open the browser on the problem statement
open "https://adventofcode.com/$YEAR/day/$NON_PADDED_DAY"

# Wait for user to copy the example input and write it to the example file
EXAMPLE_FILE="input/day$DAY/example"
if [ ! -f "$EXAMPLE_FILE" ]; then
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
echo "- input/day$DAY/example"
echo "- input/day$DAY/input"
echo "- src/bin/day$DAY.rs"
