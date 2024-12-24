use aoc2020::print_answers;

fn main() {
    print_answers(solve(include_str!("../../input/day02/input")));
}

fn solve(input: &str) -> (u32, u32) {
    let mut ans1 = 0;
    let mut ans2 = 0;

    for line in input.lines() {
        let (requirement, pass) = line.split_once(": ").unwrap();
        let (range, char) = requirement.split_once(' ').unwrap();
        let char = char.chars().nth(0).unwrap();
        let (from, to) = range.split_once('-').unwrap();
        let from = from.parse::<usize>().unwrap();
        let to = to.parse::<usize>().unwrap();

        let num = pass.chars().filter(|c| c.eq(&char)).count();
        if from <= num && num <= to {
            ans1 += 1
        }
        
        let from_char = pass.chars().nth(from-1).unwrap(); 
        let to_char = pass.chars().nth(to-1).unwrap(); 
        
        if from_char.eq(&char) ^ to_char.eq(&char) {
            ans2 += 1
        }
    }

    (ans1, ans2)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_input_own() {
        let (part1_answer, part2_answer) = solve(include_str!("../../input/day02/input"));
        assert_eq!(part1_answer, 456);
        assert_eq!(part2_answer, 218767230);
    }

    #[test]
    fn test_input_example() {
        let (part1_answer, part2_answer) = solve(include_str!("../../input/day02/example"));
        assert_eq!(part1_answer, 2);
        assert_eq!(part2_answer, 1);
    }
}