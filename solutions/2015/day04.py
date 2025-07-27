import hashlib

from solutions.abstract_solution import Solution


class Day04(Solution):
    """
        >>> Day04(2015, 4, 'abcdef').solve_part_1()
        609043
        >>> Day04(2015, 4, 'pqrstuv').solve_part_1()
        1048970
    """

    def __init__(self, year: int, day: int, input_data: str = None):
        super().__init__(year, day, input_data)

    def solve_part_1(self) -> int:
        number = -1
        while True:
            number += 1
            hash_string = hashlib.md5(f'{self.input}{number}'.encode()).hexdigest()
            if hash_string.startswith('00000'):
                break
        return number

    def solve_part_2(self) -> int:
        number = -1
        while True:
            number += 1
            hash_string = hashlib.md5(f'{self.input}{number}'.encode()).hexdigest()
            if hash_string.startswith('000000'):
                break
        return number


if __name__ == "__main__":
    import doctest

    doctest.testmod()
