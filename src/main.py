from tkinter import Tk, BOTH, Canvas
from window import Window
from line import Line, Point


def main():
    win = Window(800, 600)
    line1 = Line(Point(0,0), Point(800,600))
    line2 = Line(Point(800,0), Point(0,600))
    win.draw_line(line1, "red")
    win.draw_line(line2, "blue")
    win.wait_for_close()
    print("Bye!")


if __name__ == "__main__":
    main()

