import unittest
from Kvadrat import Square

class Tests(unittest.TestCase):

    def test_file1_area(self):
        sq = Square(2)
        assert sq.area() == 4, f"area for side {sq.side} units is {sq.area()}"
    
    def test_file1_perimeter(self):
        sq = Square(-1)
        assert sq.perimeter() == -4, f'perimeter is shown {sq.perimeter()} rather than -1'

if __name__ == '__main__':
    unittest.main()
    