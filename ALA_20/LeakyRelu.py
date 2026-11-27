import numpy as np
import unittest

def leakyrelu(x,alpha = 0.01):
    return np.where(x > 0,x,alpha * x)

class TestLeakyrelu(unittest.TestCase):
    def setUp(self):
        self.x = np.asarray([10,15,28,-10,-7,30],dtype = float)

    def test(self):
        actual = leakyrelu(self.x)
        expected = np.where(self.x>0,self.x,0.01 * self.x)

        np.testing.assert_equal(actual,expected)

if __name__ == "main":
    unittest.main()