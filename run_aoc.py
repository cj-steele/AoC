import argparse

from solutions.abstract_solution import Solution


def main():
    parser = argparse.ArgumentParser(description='Run Advent of Code solutions')
    parser.add_argument('year', type=int, help='Year (e.g., 2015)')
    parser.add_argument('day', type=int, help='Day (1-25)')
    parser.add_argument('--input', type=str, help='Input data')
    args = parser.parse_args()
    Solution.run_solution(args.year, args.day, args.input)


if __name__ == '__main__':
    main()
