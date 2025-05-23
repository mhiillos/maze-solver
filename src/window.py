from tkinter import Tk, BOTH, Canvas
from line import Line
from constants import *

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.width = width
        self.height = height
        self.canvas = Canvas(height=self.height, width=self.width, bg=BACKGROUND_COLOR)
        self.canvas.pack()
        self.running = False

    def redraw(self):
        self.canvas.update_idletasks()
        self.canvas.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)
        

