import unittest

from maze import Maze


class Tests(unittest.TestCase):
    # def test_maze_create_cells(self):
    #     num_cols = 12
    #     num_rows = 10
    #     m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    #     self.assertEqual(len(m1._Maze__cells), num_cols)
    #     self.assertEqual(len(m1._Maze__cells[0]), num_rows)
    #
    # def test_maze_create_small_grid(self):
    #     num_cols = 2
    #     num_rows = 4
    #     m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    #     self.assertEqual(len(m1._Maze__cells), num_cols)
    #     self.assertEqual(len(m1._Maze__cells[0]), num_rows)
    #
    # def test_maze_create_large_grid(self):
    #     num_cols = 50
    #     num_rows = 60
    #     m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    #     self.assertEqual(len(m1._Maze__cells), num_cols)
    #     self.assertEqual(len(m1._Maze__cells[0]), num_rows)
    #
    # def test_maze_create_even_grid(self):
    #     num_cols = 10
    #     num_rows = 10
    #     m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    #     self.assertEqual(len(m1._Maze__cells), num_cols)
    #     self.assertEqual(len(m1._Maze__cells[0]), num_rows)
    #
    # unit test for the __break_entrance_and_ext()
    def test_maze_break_entrance_and_exit(self):
        num_rows = 5
        num_cols = 5
        cell_size = 20

        maze = Maze(0, 0, num_rows, num_cols, cell_size, cell_size, win=None)

        entrance_cell = maze._Maze__cells[0][0]
        self.assertFalse(entrance_cell.has_top_wall, "Top wall of entrance cell ")

        exit_cell = maze._Maze__cells[num_cols - 1][num_rows - 1]
        self.assertFalse(
            exit_cell.has_bottom_wall, "Bottom wall of exit cell should be removed."
        )

        # self.assertTrue(entrance_cell.has_bottom_wall)
        # self.assertTrue(entrance_cell.has_right_wall)
        # self.assertTrue(exit_cell.has_top_wall)
        # self.assertTrue(exit_cell.has_left_wall)

    def test_reset_cells_visited(self):
        num_rows = 5
        num_cols = 5
        maze = Maze(
            x1=0,
            y1=0,
            num_rows=num_rows,
            num_cols=num_cols,
            cell_size_x=10,
            cell_size_y=10,
            win=None,
            seed=None,
        )

        maze._Maze__cells[0][0].visited = True
        maze._Maze__cells[2][3].visited = True
        maze._Maze__cells[num_cols - 1][num_rows - 1].visited = True
        maze._Maze__cells[1][1].visited = True

        self.assertTrue(maze._Maze__cells[0][0].visited)
        self.assertTrue(maze._Maze__cells[2][3].visited)
        self.assertTrue(maze._Maze__cells[num_cols - 1][num_rows - 1].visited)
        self.assertTrue(maze._Maze__cells[1][1].visited)

        maze._reset_cells_visited()

        for i in range(num_cols):
            for j in range(num_rows):
                self.assertFalse(
                    maze._Maze__cells[i][j].visited,
                    f"Cell at ({i}, {j}) should be unvisited after reset",
                )


if __name__ == "__main__":
    unittest.main()
