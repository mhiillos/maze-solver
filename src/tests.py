import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )
        self.assertEqual(m1._cells[0][1]._y2, 20)
        self.assertEqual(m1._cells[3][0]._x1, 30)

    def test_maze_break_entrance_and_exit(self):
        num_cols = 10
        num_rows = 10
        m = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m._cells[0][0].top_wall,
            False
        )
        self.assertEqual(
            m._cells[-1][-1].bottom_wall,
            False
        )

    def test_maze_visited_reset(self):
        num_cols = 10
        num_rows = 10
        m = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in m._cells:
            for cell in col:
                self.assertEqual(cell._visited, False)



if __name__ == "__main__":
    unittest.main()
