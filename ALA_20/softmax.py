import numpy as np
import unittest

def softmax(x):
    x_min = x - np.max(x)

    exp_values  = np.exp(x_min)
    probabilities  = exp_values / np.sum(exp_values)
    print(probabilities)

    return probabilities

class Testsoftmax(unittest.TestCase):
    def setUp(self):
        self.x = np.asarray([1,5,3,2,8,2],dtype=float)

    def test(self):
        output = softmax(self.x)
        # expected = np.asarray([8.58327156e-04,4.68630749e-02,6.34222751e-03,2.33317511e-03,9.41270020e-01,2.33317511e-03],dtype = float)

        # np.testing.assert_allclose(output,expected)

        self.assertAlmostEqual(np.sum(output),1.0)

    def test_large_values(self):
        result = softmax([1000, 1001, 1002])
        self.assertTrue(np.all(np.isfinite(result)))
        self.assertAlmostEqual(np.sum(result), 1.0)

if __name__ == "main":
    unittest.main()



