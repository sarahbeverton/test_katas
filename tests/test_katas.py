import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(4, 2), 6)
        self.assertEqual(katas.add(-3, 0), -3)
        self.assertEqual(katas.add(100.5, 0.2), 100.7)

    def test_multiply(self):
        self.assertEqual(katas.multiply(3, 5), 15)
        self.assertEqual(katas.multiply(-2, 8), -16)
        self.assertEqual(katas.multiply(0, 5), 0)

    def test_power(self):
        self.assertEqual(katas.power(2, 3), 8)
        self.assertEqual(katas.power(-3, 2), 9)
        self.assertEqual(katas.power(8, 0), 1)
        self.assertEqual(katas.power(0, 14), 0)

    def test_factorial(self):
        self.assertEqual(katas.factorial(5), 120)
        self.assertEqual(katas.factorial(1), 1)
        self.assertEqual(katas.factorial(7), 5040)

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(8), 13)
        self.assertEqual(katas.fibonacci(6), 5)
        self.assertEqual(katas.fibonacci(2), 1)


if __name__ == '__main__':
    unittest.main()
