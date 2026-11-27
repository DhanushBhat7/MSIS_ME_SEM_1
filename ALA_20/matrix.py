
import numpy as np
import unittest

def construct_D(n):

    D = np.zeros((n, n-1), dtype=np.float64)

    D[np.arange(n-1), np.arange(n-1)] = -1
    D[np.arange(1, n), np.arange(n-1)] = 1

    return D

def subvector(x, i, j):
    return x[i-1:j]

def calculate_difference(x):
    return subvector(x, 2, 6) - subvector(x, 1, 5)


class TestDifferenceMatrix(unittest.TestCase):

    def setUp(self):
        self.x = np.array(
            [1, 4, 9, 16, 25, 36],
            dtype=np.float64
        )

    def test_D(self):
        D = construct_D(6)
        self.assertEqual(D.shape, (6, 5))

    def test_subvector(self):
        result = subvector(self.x, 2, 5)
        expected = np.array([4, 9, 16, 25])
        np.testing.assert_array_equal(result, expected)

    def test_difference(self):
        D = construct_D(6)
        d1 = calculate_difference(self.x)
        d2 = D.T @ self.x
        np.testing.assert_allclose(d1, d2)

def question2():

    X = np.random.default_rng(0).standard_normal((6, 768))
    D = construct_D(6)
    result = D.T @ X

    print("X shape:", X.shape)
    print("D shape:", D.shape)
    print(X)
    print("Result shape:", result.shape)

if __name__ == "__main__":
    unittest.main(exit=False)
    question2()
