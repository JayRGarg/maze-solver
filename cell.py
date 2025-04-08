from line import Point, Line
from window import Window

class Cell:

    def __init__(self, x1, y1, x2, y2, win=None):
        self.has_left_wall:bool = True
        self.has_right_wall:bool = True
        self.has_top_wall:bool = True
        self.has_bottom_wall:bool = True
        #top-left to bottom-right coordinates
        self._x1:int = x1
        self._x2:int = x2
        self._y1:int = y1
        self._y2:int = y2
        self._center:Point = Point(round((self._x1+self._x2)/2), round((self._y1+self._y2)/2))
        self._win:Window|None = win
        self.visited = False

    def draw(self):
        left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        if self.has_left_wall:
            self._win.draw_line(left_wall, "black")
        else:
            self._win.draw_line(left_wall, "#d9d9d9")

        if self.has_top_wall:
            self._win.draw_line(top_wall, "black")
        else:
            self._win.draw_line(top_wall, "#d9d9d9")

        if self.has_right_wall:
            self._win.draw_line(right_wall, "black")
        else:
            self._win.draw_line(right_wall, "#d9d9d9")

        if self.has_bottom_wall:
            self._win.draw_line(bottom_wall, "black")
        else:
            self._win.draw_line(bottom_wall, "#d9d9d9")

    def draw_move(self, to_cell, undo=False):
        move = Line(self._center, to_cell._center)
        color = "gray" if undo else "red"
        self._win.draw_line(move, color)
