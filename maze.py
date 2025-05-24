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
        self.__cells = []
        self.__create_cells()

    def __create_cells(self):
        print(
            f"DEBUG: __create_cells - num_cols: {self.num_cols}, num_rows: {self.num_rows}"
        )
        self.__cells = [[] for _ in range(self.num_cols)]
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                new_cell = Cell(self.win, self.cell_size_x)
                self.__cells[i].append(new_cell)
            print(
                f"DEBUG: Column {i} populated. len(self.__cells[{i}])={len(self.__cells[i])}"
            )
        print(f"DEBUG: Finished populating. len(self.__cells)={len(self.__cells)}")
        if self.num_cols > 0:
            print(f"DEBUG: len(self.__cells[0])={len(self.__cells[0])}")
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                print(f"DEBUG: Drawing cell at i={i}, j={j}")
                cell_to_draw = self.__cells[i][j]
                self.__draw_cell(i, j, cell_to_draw)

    def __draw_cell(self, i, j, cell_obj):
        x_pos = self.x1 + i * self.cell_size_x
        y_pos = self.y1 + j * self.cell_size_y
        cell_obj.draw(x_pos, y_pos)
        self.animate()

    def animate(self):
        self.win.redraw()
        time.sleep(0.05)
