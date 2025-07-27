from solutions.abstract_solution import Solution


class Day03(Solution):
    """
        >>> Day03(2015, 3, '>').solve_part_1()
        2
        >>> Day03(2015, 3, '^>v<').solve_part_1()
        4
        >>> Day03(2015, 3, '^v^v^v^v^v').solve_part_1()
        2

        >>> Day03(2015, 3, '^v').solve_part_2()
        3
        >>> Day03(2015, 3, '^>v<').solve_part_2()
        3
        >>> Day03(2015, 3, '^v^v^v^v^v').solve_part_2()
        11
    """

    def __init__(self, year: int, day: int, input_data: str = None):
        super().__init__(year, day, input_data)

    def move(self, direction: str) -> tuple[int, int]:
        directions = {'^': (0, 1), 'v': (0, -1), '>': (1, 0), '<': (-1, 0)}
        return directions[direction]

    def solve_part_1(self) -> int:
        houses = {(0, 0)}
        x, y = 0, 0
        for direction in self.input:
            dx, dy = self.move(direction)
            x += dx
            y += dy
            houses.add((x, y))
        return len(houses)

    def solve_part_2(self) -> int:
        houses = {(0, 0)}
        x1, y1 = x2, y2 = 0, 0
        for i in range(0, len(self.input) - 1, 2):
            dx, dy = self.move(self.input[i])
            x1 += dx
            y1 += dy
            houses.add((x1, y1))

            dx, dy = self.move(self.input[i + 1])
            x2 += dx
            y2 += dy
            houses.add((x2, y2))
        return len(houses)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
