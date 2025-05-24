from tkinter import Tk, BOTH, Canvas
import tkinter as tk
import time


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        # it initializes data members for all its inputs
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        # This will hold list of lists of cells
        self.__cells = []
        # it calls the self.__create_cells()
        # to create the cells in the maze
        self.__create_cells()

    def __create_cells(self):
        # this fills in the __cells data member:
        # a 2-dimensional list of Cell objects.
        # It should use the number of columns and rows to figure out how
        # many Cell objects to create

        print(
            f"DEBUG: __create_cells - num_cols: {self.num_cols}, num_rows: {self.num_rows}"
        )

        self.__cells = [[] for _ in range(self.num_cols)]

        for i in range(self.num_cols):
            # current_column_cells = []
            for j in range(self.num_rows):
                # I made the top level list the columns, and the inner lists the rows
                # So self.__cells[0][0] is the top left cell,
                # and self.__cells[1][0] is the cell to the right of it.
                # new_cell = Cell(i, j)
                new_cell = Cell(self.win, self.cell_size_x)
                self.__cells[i].append(new_cell)
                # current_column_cells.append(new_cell)
            print(
                f"DEBUG: Column {i} populated. len(self.__cells[{i}])={len(self.__cells[i])}"
            )

            print(f"DEBUG: Finished populating. len(self.__cells)={len(self.__cells)}")

            if self.num_cols > 0:
                print(f"DEBUG: len(self.__cells[0])={len(self.__cells[0])}")

        # self.__cells.append(current_column_cells)
        # After creating the cells, it should call the self.__draw_cell()
        # method to draw them on the screen (we're about to create this method)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                print(f"DEBUG: Drawing cell at i={i}, j={j}")
                cell_to_draw = self.__cells[i][j]
                self.__draw_cell(i, j, cell_to_draw)

    # given i (column) and j (row)
    def __draw_cell(self, i, j, cell_obj):
        # this should calculate the x/y position of the cell
        # based on the i/j position and the cell size
        # draw the cell using the Cell's draw() method
        # Call the self._animate() method to animate the drawing of the cell
        x_pos = self.x1 + i * self.cell_size_x
        y_pos = self.y1 + j * self.cell_size_y

        cell_obj.draw(x_pos, y_pos)
        self.animate()

    # this is what allows us to visualize what the algorithms
    # are doing in real time.
    # It's not exactly performant, but it's nice to be able to see
    # what's happening as it's happening.
    # It's not only pretty, but it's good for debugging!
    # You can speed it up or slow it down by changing the sleep time
    def animate(self):
        # call the window's redraw() method
        # sleep for a short amount of time (0.05) so that
        # we can see the pretty animation
        self.win.redraw()

        time.sleep(0.05)


class Cell:
    def __init__(self, window=None, cell_size):
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

    # draw() method updates it's internal x/y coordinates
    # and draws itself on the canvas
    # it should accept new x/y coordinates as inputs
    def draw(self, x, y):
        # and set the __x1, __y1, __x2 and __y2 data members
        self.__x1 = x
        self.__y1 = y
        self.__x2 = x + self.cell_size
        self.__y2 = y + self.cell_size

        # then, if the cell has a left wall, draw it using Lines and Points
        # If the cell has a top wall, draw it,
        # and so on and so forth for each wall
        # Left wall
        p1_left = Point(self.__x1, self.__y1)
        p2_left = Point(self.__x1, self.__y2)

        # Right wall
        p1_right = Point(self.__x2, self.__y1)
        p2_right = Point(self.__x2, self.__y2)

        # Top wall
        p1_top = Point(self.__x1, self.__y1)
        p2_top = Point(self.__x2, self.__y1)

        # Bottom wall
        p1_bottom = Point(self.__x1, self.__y2)
        p2_bottom = Point(self.__x2, self.__y2)

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

    # instead of your main function just drawing a couple of lines,
    # create a few cells and draw them!
    # Test different combinations of walls to make sure they draw correctly

    # this should draw a line from the center of one cell
    # to the center of another
    def draw_move(self, to_cell, undo=False):
        # if the undo is not set, the line you draw should be "red"
        # otherwise, make it "gray"
        fill_color = "gray" if undo else "red"
        # this way as we're drawing a path through the maze,
        # it will be a nice red color, but if we need to backtrack, it will be gray
        # Use the x/y coordinates of the 2 cells in question to
        # decide how to draw the line connecting the two cells
        self_center_x = self.__x1 + self.cell_size / 2
        self_center_y = self.__y1 + self.cell_size / 2

        to_cell_center_x = to_cell.__x1 + to_cell.cell_size / 2
        to_cell_center_y = to_cell.__y1 + to_cell.cell_size / 2

        p1 = Point(self_center_x, self_center_y)
        p2 = Point(to_cell_center_x, to_cell_center_y)

        move_line = Line(p1, p2)

        self.__win.draw_line(move_line, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_one, point_two):
        self.point_one = point_one
        self.point_two = point_two

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.point_one.x,
            self.point_one.y,
            self.point_two.x,
            self.point_two.y,
            fill=fill_color,
            width=2,
        )


# create a new Window class, its constructor should
class Window:
    # take a width and height as parameters
    # this will be the size of the new window we create in pixels
    def __init__(self, width, height):
        # it should create a new root widget using Tk() and save it as a data member
        self.root = tk.Tk()

        # set the title property of the root widget
        self.root.title("My Awesome Window")

        # create a canvas widget and save it as a data member
        self.canvas = tk.Canvas(self.root, width=width, height=height, bg="white")

        # Pack the canvas widget so that it's ready to be drawn
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Create a data member to represent that the window is "running",
        # and set it to False
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    # Add a redraw() method to the Window class. It should redraw all the
    # graphics in the window (the assumption is their positions and colors
    # and such may have changed).
    # Note: Tkinter is not a reactive framework like React or Vue - we need
    # to tell the window when it should render to visuals.
    # Use the root widget's update_idletasks() and update() methods to accomplish this.

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    # Add a wait_for_close() method to the Window class. This method should:
    # Set the running state to True
    # Call self.redraw() over and over as long as the running state remais True

    def wait_for_close(self):
        # self.running = True
        # while self.running:
        #     self.redraw()
        print("Window is now running and waiting for close...")
        self.root.mainloop()
        print("Window mainloop has exited.")

    # Add a close() method to the Window class. This method should:
    def close(self):
        # Set the running state to False
        self.running = False
        # Call the root widget's protocol method to connect your close
        # method to the "delete window" action. This will stop your
        # program from running when you close the graphical window.
        # self.root.protocol("WM_DELETE_WINDOW", self.close)
        print("Closing sequence initiated!")
        self.root.destroy()

    # draw_line method to the Window class
    # this takes an instance of a Line and a fill_color as inputs
    # then call the Line's draw() method
    def draw_line(self, line_obj, fill_color="black"):
        line_obj.draw(self.canvas, fill_color)

    # self.__root = Tk()
    # ...
    # self.__root.protocol("WM_DELETE_WINDOW", self.close)

    # Create a main entrypoint function, and in it, create a window and wait for it to close:
    # win = Window(800, 600)
    # win.wait_for_close()


def main():
    CELL_SIZE = 50
    CELL_SPACING = 10
    STEP = CELL_SIZE + CELL_SPACING
    win = Window(800, 600)
    # Draw a few lines on the window using your new methods
    # in your main function, then test the program manually
    # point1 = Point(50, 50)
    # point2 = Point(200, 200)
    # my_line = Line(point1, point2)
    #
    # point3 = Point(100, 50)
    # point4 = Point(100, 200)
    # another_line = Line(point3, point4)
    #
    # win.draw_line(my_line, "blue")
    # win.draw_line(another_line, "red")
    #
    #
    #
    # Create and draw cells with different wall combinations to test

    # Cell 1: Default cell (all walls)
    # cell1 = Cell(win, CELL_SIZE)  # Pass CELL_SIZE to the Cell constructor
    # cell1.draw(50, 50)  # Draw at top-left (50, 50)

    # Cell 2: No left wall
    # cell2 = Cell(win, CELL_SIZE)  # Pass CELL_SIZE
    # cell2.has_left_wall = False
    # cell2.draw(50 + CELL_SIZE + 10, 50)  # Draw to the right of cell1, with some spacing

    # Cell 3: No top wall
    # cell3 = Cell(win, CELL_SIZE)  # Pass CELL_SIZE
    # cell3.has_top_wall = False
    # cell3.draw(50 + (CELL_SIZE + 10) * 2, 50)  # Draw to the right of cell2

    # Cell 4: Only left and bottom walls (simulating a corner)
    # cell4 = Cell(win, CELL_SIZE)  # Pass CELL_SIZE
    # cell4.has_right_wall = False
    # cell4.has_top_wall = False
    # cell4.draw(50, 50 + CELL_SIZE + 10)  # Draw below cell1
    #
    # Cell 5: Open passage (no walls at all)
    # cell5 = Cell(win, CELL_SIZE)  # Pass CELL_SIZE
    # cell5.has_left_wall = False
    # cell5.has_right_wall = False
    # cell5.has_top_wall = False
    # cell5.has_bottom_wall = False
    # cell5.draw(50 + CELL_SIZE + 10, 50 + CELL_SIZE + 10)  # Draw below cell2

    # Cell 6: Only top and right walls
    # cell6 = Cell(win, CELL_SIZE)  # Pass CELL_SIZE
    # cell6.has_left_wall = False
    # cell6.has_bottom_wall = False
    # cell6.draw(50 + (CELL_SIZE + 10) * 2, 50 + CELL_SIZE + 10)  # Draw below cell3

    # cell7.has_left_wall = False
    # cell7 = Cell(win, CELL_SIZE)  # Pass CELL_SIZE
    # cell7.has_bottom_wall = False
    # cell7.draw(50, 50 + STEP * 2)

    # cell8 = Cell(win, CELL_SIZE)  # Pass CELL_SIZE
    # cell7.has_left_wall = False
    # cell7.has_bottom_wall = False
    # cell8.draw(50 + STEP, 50 + STEP * 2)

    # cell9 = Cell(win, CELL_SIZE)  # Pass CELL_SIZE
    # cell7.has_left_wall = False
    # cell7.has_bottom_wall = False
    # cell9.draw(50 + STEP * 2, 50 + STEP * 2)

    # -- Test draw_move method --
    # print("\n Testing draw_move:")
    # Draw a red move from cell1 to cell2
    # print("Drawing red move from cell1 to cell2")
    # cell1.draw_move(cell2)

    # Add more test cases for draw_move
    # print("Drawing red move from cell2 to cell5")
    # cell2.draw_move(cell5)
    #
    # print("Drawing gray (undo) move from cell5 to cell2")
    # cell5.draw_move(cell2, undo=True)
    #
    # print("Drawing red move from cell5 to cell6")
    # cell5.draw_move(cell6)
    #
    # print("Drawing red move from cell6 to cell9")
    # cell6.draw_move(cell9)
    #
    # print("Drawing red move from cell7 to cell9")
    # cell7.draw_move(cell9, undo=True)
    #
    WIN_WIDTH = 800
    WIN_HEIGHT = 600
    CELL_SIZE = 50

    win = Window(WIN_WIDTH, WIN_HEIGHT)

    num_cols = 10
    num_rows = 8
    maze_start_x = 50
    maze_start_y = 50

    print(
        f"Creating a maze with {num_rows} rows and {num_cols} columns, starting at ({maze_start_x}, {maze_start_y})..."
    )
    maze = Maze(
        maze_start_x, maze_start_y, num_rows, num_cols, CELL_SIZE, CELL_SIZE, win
    )
    print("Maze cells have been created and drawn.")

    # You can now optionally test the draw_move method on cells within the maze
    # Access cells using maze._Maze__cells[column_index][row_index]
    # Note: Accessing __cells directly is generally discouraged in Python (private member),
    # but for testing or debugging, it's acceptable.
    if num_cols > 1 and num_rows > 1:
        print("\nTesting draw_move between maze cells:")
        cell_a = maze._Maze__cells[0][0]  # Top-left cell
        cell_b = maze._Maze__cells[1][0]  # Cell to the right
        cell_c = maze._Maze__cells[0][1]  # Cell below
        cell_d = maze._Maze__cells[1][1]  # Cell diagonally below

        # Draw a red path
        cell_a.draw_move(cell_b)
        cell_b.draw_move(cell_d)
        cell_d.draw_move(cell_c)

        # Draw an undo (gray) path
        cell_d.draw_move(cell_b, undo=True)

    win.wait_for_close()


if __name__ == "__main__":
    main()
