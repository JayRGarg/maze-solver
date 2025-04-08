from line import Point, Line
from cell import Cell
from window import Window
import time, random

class Maze:

    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None
            ):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        self._cells:List[List[Cell|None]] = [[None for j in range(self.num_rows)] for i in  range(self.num_cols)]
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
        if self._win:
            self._draw_cell(0, 0)
        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        if self._win:
            self._draw_cell(self.num_cols-1, self.num_rows-1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            dirs = []
            if i > 0 and not self._cells[i-1][j].visited:
                dirs.append([-1, 0])
            if i < self.num_cols-1 and not self._cells[i+1][j].visited:
                dirs.append([1, 0])
            if j > 0 and not self._cells[i][j-1].visited:
                dirs.append([0, -1])
            if j < self.num_rows-1 and not self._cells[i][j+1].visited:
                dirs.append([0, 1])
            
            if not dirs:
                if self._win: self._draw_cell(i, j)
                return
            else:
                num = random.randrange(len(dirs))
                dir = dirs[num]
                i2 = i + dir[0]
                j2 = j + dir[1]
                if dir == [-1, 0]:
                    self._cells[i][j].has_left_wall = False
                    self._cells[i2][j2].has_right_wall = False
                elif dir == [1, 0]:
                    self._cells[i][j].has_right_wall = False
                    self._cells[i2][j2].has_left_wall = False
                elif dir == [0, -1]:
                    self._cells[i][j].has_top_wall = False
                    self._cells[i2][j2].has_bottom_wall = False
                elif dir == [0, 1]:
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[i2][j2].has_top_wall = False
                else:
                    raise Exception("Invalid Direction!")

                self._break_walls_r(i2, j2)

    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False

