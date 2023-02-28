import unittest
import answer
class Testl1(unittest.TestCase):
    def testProb(self):
        actual = answer.calc_logs(["9","507 P 1000 1", "1 S 6 2", "1 P 1400 3", "1 S 8 8", "507 S 4 12", "1 P 1700 15", "1 S 7 16", "507 S 8 20"])
        self.assertEqual(actual,"507 1000 1000 6\n1 1400 1700 7")
if __name__ == '__main__':
    unittest.main()