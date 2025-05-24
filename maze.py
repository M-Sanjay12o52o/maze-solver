from cell import Cell
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
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._Maze__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()

    def __create_cells(self):
        print(
            f"DEBUG: __create_cells - num_cols: {self.num_cols}, num_rows: {self.num_rows}"
        )
        self._Maze__cells = [[] for _ in range(self.num_cols)]
        for i in range(self.num_cols):
            for j in range(self.num_rows):
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

        self.__draw_cell(entrance_cell_col, entrance_cell_row, entrance_cell)
        self.__draw_cell(exit_cell_col, exit_cell_row, exit_cell)
