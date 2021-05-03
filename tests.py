import unittest
import main


class TestMethods(unittest.TestCase):

    def test_multiply(self):
        res = main.multiply(4, 5)
        self.assertEqual(res, 4 * 5)


if __name__ == '__main__':
    unittest.main()
