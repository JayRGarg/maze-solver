from line import Point, Line
from cell import Cell
from window import Window
import time

class Maze:

    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None
            ):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win

        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        self._cells = [[None for j in range(self.num_rows)] for i in  range(self.num_cols)]
        for i in range(self.num_cols):
            x1_pos = self._x1 + i * self.cell_size_x
            x2_pos = x1_pos + self.cell_size_x
            for j in range(self.num_rows):
                y1_pos = self._y1 + j * self.cell_size_y
                y2_pos = y1_pos + self.cell_size_y

                self._cells[i][j] = Cell(x1_pos, y1_pos, x2_pos, y2_pos, self._win)

        if self._win:
            for i in range(self.num_cols):
                for j in range(self.num_rows):
                    self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self._draw_cell(self.num_cols-1, self.num_rows-1)
