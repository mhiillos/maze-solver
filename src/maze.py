import time
from cell import Cell

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._cells = []
        self._create_cells()

    def _create_cells(self):
        # Create cell
        for i in range(self._num_cols):
            column = []
            for j in range(self._num_rows):
                x1 = self._x1 + i * self._cell_size_x
                x2 = self._x1 + (i + 1) * self._cell_size_x
                y1 = self._y1 + j * self._cell_size_y
                y2 = self._y1 + (j + 1) * self._cell_size_y
                column.append(Cell(x1, y1, x2, y2, self._win))
            self._cells.append(column)

        # Draw each cell
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        cell.draw()
        self._animate()
        
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)
