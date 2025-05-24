from window import Window
from maze import Maze
# from point import Point
# from line import Line
# from cell import Cell


def main():
    CELL_SIZE = 50
    # CELL_SPACING = 10
    # STEP = CELL_SIZE + CELL_SPACING
    WIN_WIDTH = 800
    WIN_HEIGHT = 600

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

    if num_cols > 1 and num_rows > 1:
        print("\nTesting draw_move between maze cells:")
        cell_a = maze._Maze__cells[0][0]
        cell_b = maze._Maze__cells[1][0]
        cell_c = maze._Maze__cells[0][1]  # Cell below
        cell_d = maze._Maze__cells[1][1]  # Cell diagonally below

        cell_a.draw_move(cell_b)
        cell_b.draw_move(cell_d)
        cell_d.draw_move(cell_c)
        cell_d.draw_move(cell_b, undo=True)

    # Commented-out test code for individual cells
    """
    cell1 = Cell(win, CELL_SIZE)
    cell1.draw(50, 50)

    cell2 = Cell(win, CELL_SIZE)
    cell2.has_left_wall = False
    cell2.draw(50 + CELL_SIZE + 10, 50)

    cell3 = Cell(win, CELL_SIZE)
    cell3.has_top_wall = False
    cell3.draw(50 + (CELL_SIZE + 10) * 2, 50)

    cell4 = Cell(win, CELL_SIZE)
    cell4.has_right_wall = False
    cell4.has_top_wall = False
    cell4.draw(50, 50 + CELL_SIZE + 10)

    cell5 = Cell(win, CELL_SIZE)
    cell5.has_left_wall = False
    cell5.has_right_wall = False
    cell5.has_top_wall = False
    cell5.has_bottom_wall = False
    cell5.draw(50 + CELL_SIZE + 10, 50 + CELL_SIZE + 10)

    cell6 = Cell(win, CELL_SIZE)
    cell6.has_left_wall = False
    cell6.has_bottom_wall = False
    cell6.draw(50 + (CELL_SIZE + 10) * 2, 50 + CELL_SIZE + 10)

    print("\nTesting draw_move:")
    print("Drawing red move from cell1 to cell2")
    cell1.draw_move(cell2)
    print("Drawing red move from cell2 to cell5")
    cell2.draw_move(cell5)
    print("Drawing gray (undo) move from cell5 to cell2")
    cell5.draw_move(cell2, undo=True)
    print("Drawing red move from cell5 to cell6")
    cell5.draw_move(cell6)
    """

    win.wait_for_close()


if __name__ == "__main__":
    main()

