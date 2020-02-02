import calc
import unittest

class testCalc(unittest.TestCase):
    def test_add(self):
        r=calc.add(4,2)
        self.assertEqual(r,6)
    def test_sub(self):
        r=calc.sub(4,3)
        self.assertEqual(r,1)


if __name__ == '__main__':      #it help to run test progrm as normal prgrm
    unittest.main()             # without this,run=>  " python -m unittest test_calc.py "
