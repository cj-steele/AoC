import abc
import os
import sys
from typing import Type, TypeVar, Optional

import requests

T = TypeVar('T', bound='Solution')


class Solution(abc.ABC):
    def __init__(self, year: int, day: int, input_data: str):
        self.year = year
        self.day = day
        if input_data is None:
            self.input = self.get_aoc_input()
        else:
            self.input = input_data.strip()

    def get_aoc_input(self) -> Optional[str]:
        """
        Get the input for a specific Advent of Code day.
        
        Returns:
            The input text if successful, None otherwise
        """
        input_dir = os.path.join('inputs', str(self.year))
        input_file = os.path.join(input_dir, f'day{self.day:02d}_input.txt')

        try:
            with open(input_file, 'r') as f:
                return f.read()
        except FileNotFoundError:
            pass  # Input not cached, will download it

        # Download the input
        session_token = os.getenv('AOC_SESSION')
        if not session_token:
            print('Error: AOC_SESSION environment variable not set', file=sys.stderr)
            return None

        print(f'Downloading input for {self.year} day {self.day}...')
        url = f'https://adventofcode.com/{self.year}/day/{self.day}/input'
        response = requests.get(url, cookies={'session': session_token}, timeout=30)

        if response.status_code != 200:
            print(f'Error: Failed to download input (status {response.status_code})', file=sys.stderr)
            if response.status_code == 404:
                print(
                    'The input data file might not be available for this day or it might be mentioned in the task description.'
                    'Re-read the task and add the input data as a new file or commandline argument.', file=sys.stderr)
            return None

        # Save the input for future use
        os.makedirs(input_dir, exist_ok=True)
        with open(input_file, 'w') as f:
            f.write(response.text)

        return response.text

    @abc.abstractmethod
    def solve_part_1(self) -> None:
        pass

    @abc.abstractmethod
    def solve_part_2(self) -> None:
        pass

    @classmethod
    def run_solution(cls: Type[T], year: int, day: int, input_data: str = None) -> None:
        """Dynamically import and run the solution for a specific day."""
        try:
            module_name = f"solutions.{year}.day{day:02d}"
            module = __import__(module_name, fromlist=[f"Day{day:02d}"])
            solution_class = getattr(module, f"Day{day:02d}")
            solution = solution_class(year, day, input_data)

            print(f"--- {year} Day {day} ---")
            print("Part 1:", solution.solve_part_1())
            if hasattr(solution, 'solve_part_2'):
                print("Part 2:", solution.solve_part_2())

        except (ImportError, AttributeError) as e:
            print(f"Error: Could not find solution for {year} day {day}")
            print(f"Details: {str(e)}")
