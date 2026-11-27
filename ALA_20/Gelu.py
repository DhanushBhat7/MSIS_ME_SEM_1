import numpy as np
import unittest

def Gelu(x):
    return 0.5 * x * ( 1+ np.tanh(np.sqrt(2/np.pi)*(x+0.044715 * x **3))) 

class TestGelu(unittest.TestCase):
    def setUp(self):
        self.x = np.asarray([-1.3,4,-7,8,3,1], dtype = float)

    def test(self):
        output = Gelu(self.x)
        expected = np.asarray([0.5 * val * ( 1+ np.tanh (np.sqrt(2/np.pi)*(val+0.044715 * val **3))) for val in self.x], dtype = float)

        np.testing.assert_allclose(output,expected)

if __name__ == "main":
    unittest.main()