from window import Window
from line import Point, Line
from cell import Cell

def main():
    win = Window(800, 600)
    # p1 = Point(10, 0)
    # p2 = Point(10, 50)
    # p3 = Point(25, 50)
    # l1 = Line(p1, p2)
    # l2 = Line(p2, p3)
    # l3 = Line(p3, p1)
    # win.draw_line(l1, "black")
    # win.draw_line(l2, "red")
    # win.draw_line(l3, "red")
    c1 = Cell(10, 20, 10, 20, win)
    c1.has_right_wall = False
    c2 = Cell(20, 30, 10, 20, win)
    c2.has_left_wall = False
    c2.has_bottom_wall = False
    c3 = Cell(20, 30, 20, 30, win)
    c3. has_top_wall = False
    c1.draw()
    c2.draw()
    c3.draw()
    c1.draw_move(c2)
    c2.draw_move(c3)
    win.wait_for_close()


if __name__ == "__main__":
    main()
