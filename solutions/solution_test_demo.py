import unittest
from demo import *


class TestDemo(unittest.TestCase):

    def test_move(self):
        self.assertEqual(move(1, 6), 7)
        self.assertEqual(move(7, 5), 12)
        self.assertEqual(move(12, 4), 16)

    def test_ladders(self):
        self.assertEqual(move_ladders(12), 25)
        self.assertEqual(move_ladders(2), 16)
        self.assertEqual(move_ladders(5), 20)

    def test_snakes(self):
        self.assertEqual(move_snakes(35), 23)
        self.assertEqual(move_snakes(28), 21)
        self.assertEqual(move_snakes(22), 15)

    def test_win(self):
        self.assertEqual(win(28), 0)
        self.assertEqual(win(36), 1)
        self.assertEqual(win(40), 1)