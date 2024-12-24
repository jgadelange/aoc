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
touch "input/day$DAY/example"  # Example input file
touch "input/day$DAY/input"    # Main input file

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
if [ ! -f "src/bin/day$DAY.rs" ]; then
  echo "$RUST_TEMPLATE" > "src/bin/day$DAY.rs"
fi

# Output success message
echo "Setup complete for Day $DAY. Files created:"  
echo "- input/day$DAY/example"
echo "- input/day$DAY/input"
echo "- src/bin/day$DAY.rs"
