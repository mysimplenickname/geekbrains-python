class Cell:
    cells: int

    def __init__(self, cells: int):
        self.cells = cells

    def __add__(self, other):
        return self.cells + other.cells

    def __sub__(self, other):
        return self.cells - other.cells if self.cells - other.cells > 0 else f"The number of cells of the second cell is bigger than of the first one."

    def __mul__(self, other):
        return self.cells * other.cells

    def __truediv__(self, other):
        return self.cells // other.cells if other.cells != 0 else f"You can't divide by zero."

    def make_order(self, cells_per_row):
        return '\n'.join(['*' * cells_per_row for j in range(self.cells // cells_per_row)] + ['*' * (self.cells % cells_per_row)])


cell_1 = Cell(8)
cell_2 = Cell(5)

print(f"Sum: {cell_1 + cell_2}")
print(f"Difference: {cell_1 - cell_2}")
print(f"Multiplication: {cell_1 * cell_2}")
print(f"Division: {cell_1 / cell_2}")

print()

print("Result: ")
cell_3 = Cell(7)
print(cell_3.make_order(3))
