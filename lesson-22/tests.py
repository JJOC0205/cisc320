import unittest
from dataclasses import dataclass
import answer
class Testl1(unittest.TestCase):
    def test_normal(self):
        actual = answer.devouring(5,15,
            ["TextBook","HardDrive","DogFood","FavoriteGame","SuperComputer"],
            [4,10,10,20,100],[50,2,5,60,100])
        self.assertEqual(actual,answer.Food(55,['','TextBook','DogFood']))
        actual = answer.devouring(5,15,
            ["TextBook","HardDrive","DogFood","FavoriteGame","SuperComputer"],
            [5,10,9,15,100],[50,2,5,60,100])
        self.assertEqual(actual,answer.Food(60,['','FavoriteGame']))
    def test_over_cap(self):
        actual = answer.devouring(5,15,
            ["TextBook","HardDrive","DogFood","FavoriteGame","SuperComputer"],
            [16,17,18,20,100],[50,2,5,60,100])
        self.assertEqual(actual,answer.Food(0,['']))
        actual = answer.devouring(5,0,
            ["TextBook","HardDrive","DogFood","FavoriteGame","SuperComputer"],
            [16,17,18,20,100],[50,2,5,60,100])
        self.assertEqual(actual,answer.Food(0,['']))
    def test_all_fit(self):
        actual = answer.devouring(5,300,
            ["TextBook","HardDrive","DogFood","FavoriteGame","SuperComputer"],
            [4,10,10,20,100],[50,2,5,60,100])
        self.assertEqual(actual,answer.Food(217,['',"TextBook","HardDrive","DogFood","FavoriteGame","SuperComputer"]))
   
if __name__ == '__main__':
    unittest.main()