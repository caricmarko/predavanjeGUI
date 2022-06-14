from Kvadrat import Square
import unittest
  
class TestSum(unittest.TestCase):
  
    def test_area(self):
        sq = Square(2)
  
        self.assertEqual(sq.area(), 5, 
            f'Area is shown {sq.area()} rather than 9')
  
if __name__ == '__main__':
    unittest.main()