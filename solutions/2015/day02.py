from solutions.abstract_solution import Solution


class Day02(Solution):
    """
        >>> Day02(2015, 2, '2x3x4').solve_part_1()
        58
        >>> Day02(2015, 2, '1x1x10').solve_part_1()
        43

        >>> Day02(2015, 2, '2x3x4').solve_part_2()
        34
        >>> Day02(2015, 2, '1x1x10').solve_part_2()
        14
    """

    def __init__(self, year: int, day: int, input_data: str = None):
        super().__init__(year, day, input_data)

    def parse_input(self, line: str) -> list[int]:
        l, w, h = line.split('x')
        return [int(l), int(w), int(h)]

    def solve_part_1(self) -> int:
        total_paper = 0
        for line in self.input.splitlines():
            l, w, h = self.parse_input(line)
            left = l * h
            front = w * h
            top = l * w
            smallest = min(left, front, top)
            total_paper += 2 * left + 2 * front + 2 * top + smallest
        return total_paper

    def solve_part_2(self) -> int:
        total_ribbon = 0
        for line in self.input.splitlines():
            l, w, h = self.parse_input(line)
            left = l * 2 + h * 2
            front = w * 2 + h * 2
            top = l * 2 + w * 2
            smallest = min(left, front, top)
            volume = l * w * h
            total_ribbon += smallest + volume
        return total_ribbon


if __name__ == "__main__":
    import doctest

    doctest.testmod()
