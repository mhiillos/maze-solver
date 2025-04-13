from line import Line, Point
from window import Window

class Cell():
    def __init__(self, x1, y1, x2, y2, win, left_wall=True, right_wall=True, top_wall=True, bottom_wall=True):
        self.left_wall = left_wall
        self.right_wall = right_wall
        self.top_wall = top_wall
        self.bottom_wall = bottom_wall
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win

    def draw(self):
        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bottom_left = Point(self._x1, self._y2)
        bottom_right = Point(self._x2, self._y2)
        lines = []
        if self.left_wall:
            lines.append(Line(top_left, bottom_left))
        if self.right_wall:
            lines.append(Line(top_right, bottom_right))
        if self.top_wall:
            lines.append(Line(top_left, top_right))
        if self.bottom_wall:
            lines.append(Line(bottom_left, bottom_right))

        for line in lines:
            print(line)
            self._win.draw_line(line, "black")

