from cell import Cell
import time
import random


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
        seed=None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._Maze__cells = []

        if seed is not None:
            random.seed(seed)

        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self._reset_cells_visited()

    def __create_cells(self):
        print(
            f"DEBUG: __create_cells - num_cols: {self.num_cols}, num_rows: {self.num_rows}"
        )
        self._Maze__cells = [[] for _ in range(self.num_cols)]
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                # new_cell = Cell(self.win, self.cell_size_x, self.cell_size_y)
                new_cell = Cell(self.win, self.cell_size_x)
                self._Maze__cells[i].append(new_cell)
            print(
                f"DEBUG: Column {i} populated. len(self._Maze__cells[{i}])={len(self._Maze__cells[i])}"
            )
        print(
            f"DEBUG: Finished populating. len(self._Maze__cells)={len(self._Maze__cells)}"
        )
        if self.num_cols > 0:
            print(f"DEBUG: len(self._Maze__cells[0])={len(self._Maze__cells[0])}")

        if self.win is not None:
            for i in range(self.num_cols):
                for j in range(self.num_rows):
                    print(f"DEBUG: Drawing cell at i={i}, j={j}")
                    cell_to_draw = self._Maze__cells[i][j]
                    self.__draw_cell(i, j, cell_to_draw)

    def __draw_cell(self, i, j, cell_obj):
        x_pos = self.x1 + i * self.cell_size_x
        y_pos = self.y1 + j * self.cell_size_y
        cell_obj.draw(x_pos, y_pos)
        self.animate()

    def animate(self):
        if self.win is not None:
            self.win.redraw()
        time.sleep(0.05)

    def __break_entrance_and_exit(self):
        entrance_cell_col = 0
        entrance_cell_row = 0
        entrance_cell = self._Maze__cells[entrance_cell_col][entrance_cell_row]
        entrance_cell.has_top_wall = False

        exit_cell_col = self.num_cols - 1
        exit_cell_row = self.num_rows - 1
        exit_cell = self._Maze__cells[exit_cell_col][exit_cell_row]
        exit_cell.has_bottom_wall = False

        if self.win is not None:
            self.__draw_cell(entrance_cell_col, entrance_cell_row, entrance_cell)
            self.__draw_cell(exit_cell_col, exit_cell_row, exit_cell)

    # this is a recursive method.
    # its a depth-first traversal through the cells
    # breaking down walls as it goes.
    def __break_walls_r(self, i, j):
        current_cell = self._Maze__cells[i][j]
        current_cell.visited = True

        while True:
            unvisited_neighbors = []

            if i > 0 and not self._Maze__cells[i - 1][j].visited:
                unvisited_neighbors.append((i - 1, j, "top"))
            if j < self.num_rows - 1 and not self._Maze__cells[i][j + 1].visited:
                unvisited_neighbors.append((i, j + 1, "right"))
            if i < self.num_cols - 1 and not self._Maze__cells[i + 1][j].visited:
                unvisited_neighbors.append((i + 1, j, "bottom"))
            if j > 0 and not self._Maze__cells[i][j - 1].visited:
                unvisited_neighbors.append((i, j - 1, "left"))

            if not unvisited_neighbors:
                return

            next_cell_info = random.choice(unvisited_neighbors)
            next_i, next_j, direction = next_cell_info
            next_cell = self._Maze__cells[next_i][next_j]

            if direction == "top":
                current_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
            elif direction == "right":
                current_cell.has_right_wall = False
                next_cell.has_left_wall = False
            elif direction == "bottom":
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
            elif direction == "left":
                current_cell.has_left_wall = False
                next_cell.has_right_wall = False

            if self.win is not None:
                self.__draw_cell(i, j, current_cell)
                self.__draw_cell(next_i, next_j, next_cell)

            self.__break_walls_r(next_i, next_j)

    def _reset_cells_visited(self):
        for col_index in range(self.num_cols):
            for row_index in range(self.num_rows):
                self._Maze__cells[col_index][row_index].visited = False
