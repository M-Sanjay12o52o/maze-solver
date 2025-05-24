from point import Point
from line import Line


class Cell:
    def __init__(self, window=None, cell_size=50):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window
        self.cell_size = cell_size

    def draw(self, x, y):
        self.__x1 = x
        self.__y1 = y
        self.__x2 = x + self.cell_size
        self.__y2 = y + self.cell_size

        p1_left = Point(self.__x1, self.__y1)
        p2_left = Point(self.__x1, self.__y2)
        p1_right = Point(self.__x2, self.__y1)
        p2_right = Point(self.__x2, self.__y2)
        p1_top = Point(self.__x1, self.__y1)
        p2_top = Point(self.__x2, self.__y1)
        p1_bottom = Point(self.__x1, self.__y2)
        p2_bottom = Point(self.__x2, self.__y2)

        if self.__win is not None:
            if self.has_left_wall:
                line = Line(p1_left, p2_left)
                self.__win.draw_line(line, "black")

            if self.has_right_wall:
                line = Line(p1_right, p2_right)
                self.__win.draw_line(line, "black")

            if self.has_top_wall:
                line = Line(p1_top, p2_top)
                self.__win.draw_line(line, "black")

            if self.has_bottom_wall:
                line = Line(p1_bottom, p2_bottom)
                self.__win.draw_line(line, "black")

    def draw_move(self, to_cell, undo=False):
        fill_color = "gray" if undo else "red"
        self_center_x = self.__x1 + self.cell_size / 2
        self_center_y = self.__y1 + self.cell_size / 2
        to_cell_center_x = to_cell.__x1 + to_cell.cell_size / 2
        to_cell_center_y = to_cell.__y1 + to_cell.cell_size / 2
        p1 = Point(self_center_x, self_center_y)
        p2 = Point(to_cell_center_x, to_cell_center_y)

        if self.__win is not None:
            move_line = Line(p1, p2)
            self.__win.draw_line(move_line, fill_color)
