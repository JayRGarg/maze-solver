from window import Window
from line import Point, Line

def main():
    win = Window(800, 600)
    p1 = Point(10, 0)
    p2 = Point(10, 50)
    p3 = Point(25, 50)
    l1 = Line(p1, p2)
    l2 = Line(p2, p3)
    l3 = Line(p3, p1)
    win.draw_line(l1, "black")
    win.draw_line(l2, "red")
    win.draw_line(l3, "red")
    win.wait_for_close()


if __name__ == "__main__":
    main()
