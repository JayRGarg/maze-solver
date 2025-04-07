from line import Point, Line
from window import Window

class Cell:

    def __init__(self, x1, x2, y1, y2, win):
        self.has_left_wall:bool = True
        self.has_right_wall:bool = True
        self.has_top_wall:bool = True
        self.has_bottom_wall:bool = True
        #top-left to bottom-right coordinates
        self._x1:int = x1
        self._x2:int = x2
        self._y1:int = y1
        self._y2:int = y2
        self._win:Window = win

    def draw(self):
        if self.has_left_wall:
            left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(left_wall, "black")
        if self.has_top_wall:
            top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(top_wall, "black")
        if self.has_right_wall:
            right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(right_wall, "black")
        if self.has_bottom_wall:
            bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(bottom_wall, "black")
