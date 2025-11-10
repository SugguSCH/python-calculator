import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    #add 1
    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    #add 2
    def test_add_neg(self):
        self.assertEqual(self.calc.add(-5, -2), -7)

    #sub 1 Error
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(-9, 2), -11)

    #sub 2 Error
    def test_subtract_neg(self):
        self.assertEqual(self.calc.subtract(9, -2), 11)
    
    #mul 1 Error
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(-9, 5), -45)

    #mul 2 Error
    def test_multiply_neg(self):
        self.assertEqual(self.calc.multiply(9, -2), -18)

    #divide 1 Error
    def test_divide(self):
        self.assertEqual(self.calc.divide(-9, 3), -3)

    #divide 2 Error
    def test_divide_neg(self):
        self.assertEqual(self.calc.divide(18, -2), -9)

    #mod 1 Error
    def test_mod(self):
        self.assertEqual(self.calc.modulo(18, 5), 3)

    #mod 2 Error
    def test_mod_neg(self):
        self.assertEqual(self.calc.modulo(6, -4), -2)

if __name__ == '__main__':
    unittest.main()