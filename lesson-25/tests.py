import unittest
import answer
class Testl1(unittest.TestCase):
    def test_normal(self):
        data = [[0, 10, 15, 20], [10, 0, 35, 25],
            [15, 35, 0, 30], [20, 25, 30, 0]]
        actual = answer.tsp(data, 0)
        self.assertEqual(actual,([0, 1, 3, 2, 0], 80))
        actual = answer.tsp(data, 1)
        self.assertEqual(actual,([1, 0, 2, 3, 1], 80))
        actual = answer.tsp(data, 2)
        self.assertEqual(actual,([2, 0, 1, 3, 2], 80))
        actual = answer.tsp(data, 3)
        self.assertEqual(actual,([3, 0, 1, 2, 3], 95))
    def test_normal2(self):
        data = [[0,3,4,2,7], [3,0,4,6,3],[4,4,0,5,8],[2,6,5,0,6],[7,3,8,6,0]]
        actual = answer.tsp(data, 0)
        self.assertEqual(actual,([0, 3, 2, 1, 4, 0], 21))
        actual = answer.tsp(data, 1)
        self.assertEqual(actual,([1, 0, 3, 2, 4, 1], 21))
        actual = answer.tsp(data, 2)
        self.assertEqual(actual,([2, 0, 3, 1, 4, 2], 23))
        actual = answer.tsp(data, 3)
        self.assertEqual(actual,([3, 0, 1, 4, 2, 3], 21))
        actual = answer.tsp(data, 4)
        self.assertEqual(actual,([4, 1, 0, 3, 2, 4], 21))
    
    def test_empty(self):
        data = []
        actual = answer.tsp(data, 0)
        self.assertEqual(actual,([], 0))
