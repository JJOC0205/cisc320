import unittest
import answer
class Testl1(unittest.TestCase):
    def testProb(self):
        actual = answer.print_lines(["6\n","5\n","10\n","-3\n","15\n",'-999\n','13\n'])
        self.assertEqual(actual,30)
        actual = answer.print_lines(["2\n","5\n","10\n","-3\n","15\n",'-999\n','13\n'])
        self.assertEqual(actual,15)
        actual = answer.print_lines(["11\n","5\n","10\n","-3\n","15\n",'-999\n','13\n'])
        self.assertEqual(actual,30)
        actual = answer.print_lines(['3\n','0\n','0\n','0\n'])
        self.assertEqual(actual,0)
    def testEmpty(self):
        actual = answer.print_lines(['3\n','-1\n','-1\n','-1\n'])
        self.assertEqual(actual,"EMPTY")
        actual = answer.print_lines(['0\n','1\n','1\n','-1\n'])
        self.assertEqual(actual,"EMPTY")
        actual = answer.print_lines(['3\n','-999\n','1\n','-1\n'])
        self.assertEqual(actual,"EMPTY")
        actual = answer.print_lines(['5\n','-1\n','-1\n','-1\n','-999\n'])
        self.assertEqual(actual,"EMPTY")
        actual = answer.print_lines(['-999\n','37\n','-1\n','-1\n'])
        self.assertEqual(actual,"EMPTY")
if __name__ == '__main__':
    unittest.main()