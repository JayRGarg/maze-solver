from window import Window
from line import Point, Line
from cell import Cell
from maze import Maze

def main():

    win = Window(1100, 1100)
    m1 = Maze(40, 40, 25, 25, 40, 40, win)#, seed=0)
    m1.solve()
    win.wait_for_close()

    return


if __name__ == "__main__":
    main()
