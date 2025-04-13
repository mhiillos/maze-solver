from tkinter import Tk, BOTH, Canvas
from window import Window
from line import Line, Point
from cell import Cell


def main():
    win = Window(800, 600)
    line1 = Line(Point(0,0), Point(800,600))
    line2 = Line(Point(800,0), Point(0,600))
    cell1 = Cell(50,50,100,100, win)
    cell1.draw()
    cell2 = Cell(120, 120, 180, 180, win, False, True, False, True)
    cell2.draw()
    cell3 = Cell(200, 200, 210, 210, win, True, True, False, False)
    cell3.draw()

    cell1.draw_move(cell2, True)
    cell2.draw_move(cell3, False)
    win.wait_for_close()
    print("Bye!")


if __name__ == "__main__":
    main()

