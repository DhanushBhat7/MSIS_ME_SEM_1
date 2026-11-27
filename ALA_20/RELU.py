import numpy as np
import unittest

def RELU(x):
  return np.maximum(0,x)

class TestRELU(unittest.TestCase):
    def setUp(self):
        self.x = np.asarray([-5,7,0,5,-19,19],dtype = float)

    def test(self):
        actual = RELU(self.x)
        expected = np.asarray([0,7,0,5,0,19],dtype=float)

        np.testing.assert_allclose(actual,expected)

if __name__ == "main":
  unittest.main(verbosity=2)