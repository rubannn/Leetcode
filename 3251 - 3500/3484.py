class Spreadsheet:

    def __init__(self, rows: int):
        self.cells = dict()

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        self.cells[cell] = 0

    def getValue(self, formula: str) -> int:
        items = formula[1:].split("+")
        return sum(
            int(item) if item.isdigit() else self.cells.get(item, 0) for item in items
        )


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
