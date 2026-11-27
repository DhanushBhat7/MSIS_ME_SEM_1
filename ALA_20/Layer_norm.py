import numpy as np
import unittest

def layernorm(e,gamma,beta,epsilon=1e-5):
    e = np.asarray(e,dtype=float)
    gamma = np.asarray(gamma,dtype=float)
    beta = np.asarray(beta,dtype=float)
    epsilon = np.asarray(epsilon,dtype=float)

    mean = np.sum(e)/len(e)
    var = np.sum((e-mean)**2)/len(e)
    normalized = (e-mean)/np.sqrt(var+epsilon)

    result = normalized*gamma + beta
    return result

class layernormTest(unittest.TestCase):
    def setUp(self):
        self.e = np.array([2, 4, 6, 8], dtype=float)
        self.gamma = np.ones(4)
        self.beta = np.zeros(4)
        self.epsilon = 1e-5

    def test_reference(self):
        actual = layernorm(self.e,self.gamma,self.beta,self.epsilon)
        mean = np.mean(self.e)
        var = np.var(self.e)
        expected = (self.e - mean) / np.sqrt(var + self.epsilon)

        np.testing.assert_allclose(actual, expected)

    def test_mean_var(self):
        output = layernorm(self.e,self.gamma,self.beta,self.epsilon)
        mean = np.mean(self.e)
        var = np.var(self.e)
        expected_var = var/(var+self.epsilon)

        self.assertAlmostEqual(np.mean(output), 0, places=5)
        self.assertAlmostEqual(np.var(output), expected_var, places=5)

if __name__ == "__main__":
    unittest.main()
