from solutions.abstract_solution import Solution


class Day01(Solution):
    """
        >>> Day01(2015, 1, '(())').solve_part_1()
        0
        >>> Day01(2015, 1, '()()').solve_part_1()
        0
        >>> Day01(2015, 1, '(((').solve_part_1()
        3
        >>> Day01(2015, 1, '(()(()(').solve_part_1()
        3
        >>> Day01(2015, 1, '))(((((').solve_part_1()
        3
        >>> Day01(2015, 1, '())').solve_part_1()
        -1
        >>> Day01(2015, 1, '))(').solve_part_1()
        -1
        >>> Day01(2015, 1, ')))').solve_part_1()
        -3
        >>> Day01(2015, 1, ')())())').solve_part_1()
        -3

        >>> Day01(2015, 1, ')').solve_part_2()
        1
        >>> Day01(2015, 1, '()())').solve_part_2()
        5
    """

    def __init__(self, year: int, day: int, input_data: str = None):
        super().__init__(year, day, input_data)

    def solve_part_1(self) -> int:
        return self.input.count('(') - self.input.count(')')

    def solve_part_2(self) -> int:
        floor = 0
        for i, char in enumerate(self.input, 1):
            floor += 1 if char == '(' else -1
            if floor < 0:
                return i
        return -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
