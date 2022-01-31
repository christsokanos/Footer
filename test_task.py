import unittest
from task import Footer

class TestTask(unittest.TestCase):

    def test_isValid(self):
        #Testing inputs
        self.assertTrue(Footer.isValid(0))
        self.assertTrue(Footer.isValid(1))
        self.assertTrue(Footer.isValid(99999999999999999))
        self.assertFalse(Footer.isValid(-1))
        self.assertFalse(Footer.isValid('a'))

    def test_calc(self):
        #Testing calculation
        f1 = Footer(10, 5, 1, 1)
        endbound, lside, rside = f1.calc()
        self.assertEqual(endbound, 9)
        self.assertEqual(lside, 4)
        self.assertEqual(rside, 6)

    def test_output(self):
        #Testing output
        f1 = Footer(10, 5, 1, 1)
        f1.calc()
        self.assertEqual(f1.footerOutput(), '1 ... 456 ... 10')


if __name__ == '__main__':
    unittest.main()