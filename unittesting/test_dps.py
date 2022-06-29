import unittest
import sys
sys.path.append("..")
from maths.computation import get_multiplier

class Testcomputation(unittest.TestCase):
    def test_get_multiplier(self):
        #no crit rate
        self.assertEqual(get_multiplier(c_rate=0, c_dmg=200), 1)

        #if crit if 100 or greater
        self.assertEqual(get_multiplier(100, 200), 2)
        self.assertEqual(get_multiplier(200, 200), 2)

        #kbw
        self.assertEqual(get_multiplier(100, 200, kbw=True), 1.96)

        #negative crit
        self.assertRaises(ValueError, get_multiplier, -50, 200)

if __name__ == '__main__':
    unittest.main()