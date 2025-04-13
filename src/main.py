from tkinter import Tk, BOTH, Canvas
from window import Window
from line import Line, Point
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(40, 30, 9, 12, 60, 60, win)
    maze.solve()
    win.wait_for_close()
    print("Bye!")


if __name__ == "__main__":
    main()

