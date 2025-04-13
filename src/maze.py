import time
from cell import Cell
import random

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        if seed is not None:
            random.seed(seed)

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

        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        cell.draw()
        self._animate()
        
    def _animate(self):
        if self._win:
            self._win.redraw()
            time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].bottom_wall = False
        self._draw_cell(-1, -1) 

    def _break_walls_r(self, i, j):
        opposite = {
            "top": "bottom",
            "bottom": "top",
            "left": "right",
            "right": "left",
        }
        self._cells[i][j]._visited = True
        while True:
            # Gathers the indeces i, j of cells we want to visit
            to_visit = []
            # Check adjacent cells
            indeces_to_check = [(i, j-1, "top"), (i, j+1, "bottom"), (i-1, j, "left"), (i+1, j, "right")]
            for idx_tuple in indeces_to_check:
                if not (0 <= idx_tuple[0] < len(self._cells)) or not (0 <= idx_tuple[1] < len(self._cells[i])):
                    continue
                adj_cell = self._cells[idx_tuple[0]][idx_tuple[1]]
                if not adj_cell._visited:
                    to_visit.append(idx_tuple)
            if len(to_visit) == 0:
                self._cells[i][j].draw()
                break
            else:
                # Choose random cell, break the wall between the current and the chosen cell
                next_idx = random.randrange(len(to_visit))
                setattr(self._cells[i][j], f"{to_visit[next_idx][2]}_wall", False)
                setattr(self._cells[to_visit[next_idx][0]][to_visit[next_idx][1]], f"{opposite[to_visit[next_idx][2]]}_wall", False)
                self._draw_cell(i, j)
                self._break_walls_r(to_visit[next_idx][0], to_visit[next_idx][1])

    # Reset the visited property of cells after generating the Maze
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell._visited = False

