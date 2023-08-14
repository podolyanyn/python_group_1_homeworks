# # Task 1
# from math import lcm
# import unittest
#
# class Fraction:
#
#     def __init__(self, a, b):
#         if b == 0:
#             raise ZeroDivisionError("Denominator cannot be 0!")
#         self.a = a
#         self.b = b
#
#     def __add__(self, other):
#         if isinstance(other, Fraction):
#             nsk = lcm(self.b, other.b)
#             return Fraction(int(self.a * nsk/self.b+other.a * nsk/other.b), int(nsk))
#
#     def __sub__(self, other):
#         if isinstance(other, Fraction):
#             nsk = lcm(self.b, other.b)
#             return Fraction(int(self.a * nsk/self.b-other.a * nsk/other.b),nsk)
#
#     def __mul__(self, other):
#         if isinstance(other, Fraction):
#             return Fraction(self.a * other.a, self.b * other.b)
#
#     def __truediv__(self, other):
#         if other.a == 0:
#             raise ZeroDivisionError("Denominator cannot be 0!")
#         if isinstance(other, Fraction):
#             return Fraction(self.a * other.b,self.b * other.a)
#
#     def __str__(self):
#         if self.a % 1 == 0:
#             self.a = int(self.a)
#         return f'{str(self.a)}/{self.b}'
#
#     def __eq__(self, other):
#         return self.a == other.a and self.b == other.b
#
#     def __lt__(self, other):
#         return self.a * other.b < other.a * self.b
#
#     def __gt__(self, other):
#         return self.a * other.b > other.a * self.b
#
#
# class TestFractionOperations(unittest.TestCase):
#     def test_add(self):
#         a = Fraction(1, 2)
#         b = Fraction(1, 4)
#         self.assertEqual(a + b, Fraction(3, 4))
#
#     def test_sub(self):
#         a = Fraction(1, 2)
#         b = Fraction(1, 4)
#         self.assertEqual(a - b, Fraction(1, 4))
#
#     def test_multiply(self):
#         a = Fraction(1, 2)
#         b = Fraction(1, 4)
#         self.assertEqual(a * b, Fraction(1, 8))
#
#     def test_div(self):
#         a = Fraction(1, 2)
#         b = Fraction(1, 4)
#         self.assertEqual(a / b, Fraction(4, 2))
#
#     def test_equal(self):
#         a = Fraction(1, 2)
#         b = Fraction(1, 4)
#         self.assertFalse(a == b)
#
#     def test_less_then(self):
#         a = Fraction(1, 2)
#         b = Fraction(1, 4)
#         self.assertFalse(a < b)
#
#     def test_greater_then(self):
#         a = Fraction(1, 2)
#         b = Fraction(1, 4)
#         self.assertFalse(a > b, 'a is less then b')
#
#
# if __name__ == '__main__':
#     unittest.main()