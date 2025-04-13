from tkinter import Tk, BOTH, Canvas
from window import Window
from line import Line, Point
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(80, 60, 10, 10, 40, 40, win)
    win.wait_for_close()
    print("Bye!")


if __name__ == "__main__":
    main()

