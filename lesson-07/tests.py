import unittest
import answer
class Testl1(unittest.TestCase):
    def testNormal(self):
        actual = answer.calc_logs(["8","507 P 1000 1", "1 S 6 2", "1 P 1400 3", "1 S 8 8", "507 S 4 12", "1 P 1700 15", "1 S 7 16", "507 S 8 20"])
        self.assertEqual(actual,['507 1000 1000 6', '1 1400 1700 7'])
        actual = answer.calc_logs(["12","507 P 1300 1", "1 S 6 2", "1 P 1400 3", "1 S 8 8", "507 S 4 12", "1 P 1700 15", "1 S 7 16", "507 S 8 20", "100 S 9 1", "100 P 1200 1999 2", "100 S 4 33", "100 S 4 3"])
        self.assertEqual(actual,['100 1200 1200 5', '507 1300 1300 6', '1 1400 1700 7'])
    def testEmpty(self):
        actual = answer.calc_logs(["0"])
        self.assertEqual(actual,[])
        actual = answer.calc_logs(["0", "12 S 100 3"])
        self.assertEqual(actual,[])
    def testMissing(self):
        actual = answer.calc_logs(["8","507 P 000 1", "1 S 6 2", "1 P 1400 3", "1 S 8 8", "507 S 4 12", "1 P 1700 15", "1 S 7 16", "507 S 8 20"])
        self.assertEqual(actual, ['507 000 000 6','1 1400 1700 7'])
        actual = answer.calc_logs(["8","507 S 9 1", "1 S 6 2", "1 S 1400 3", "1 S 8 8", "507 S 4 12", "1 S 1700 15", "1 S 7 16", "507 S 8 20"])
        self.assertEqual(actual, [])
if __name__ == '__main__':
    unittest.main()