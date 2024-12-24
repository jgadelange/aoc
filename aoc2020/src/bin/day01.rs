use aoc2020::print_answers;

fn main() {
    print_answers(solve(include_str!("../../input/day01/input")));
}

fn solve(input: &str) -> (u32, u32) {
    let numbers: Vec<_> = input.lines().map(|x| x.parse::<u32>().unwrap()).collect();

    let mut ans1 = 0;
    let mut ans2 = 0;
    for (i, a) in numbers.iter().enumerate() {
        for (j, b) in numbers[i + 1..].iter().enumerate() {
            if a + b == 2020 {
                ans1 = a * b;
            }
            for c in numbers[j + 1..].iter() {
                if a + b + c == 2020 {
                    ans2 = a * b * c;
                }
            }
        }
    }
    (ans1, ans2)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_input_own() {
        let (part1_answer, part2_answer) = solve(include_str!("../../input/day01/input"));
        assert_eq!(part1_answer, 1016619);
        assert_eq!(part2_answer, 218767230);
    }

    #[test]
    fn test_input_example() {
        let (part1_answer, part2_answer) = solve(include_str!("../../input/day01/example"));
        assert_eq!(part1_answer, 514579);
        assert_eq!(part2_answer, 241861950);
    }
}