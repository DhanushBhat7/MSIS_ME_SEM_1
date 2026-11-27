
import numpy as np
import unittest

def pair_score(X, Z, W):
    """
    Computes PairScore using two input matrices and parameters.

    Arguments:
        X : Input matrix of shape (6, lx).
        Z : Input matrix of shape (10, lz).
        W : Tuple (A, a, B, b) containing parameters.

    Returns:
        S : Output matrix of shape (lz, lx).
    """

    # Step 1: Convert inputs to NumPy arrays
    X = np.asarray(X, dtype=np.float64)
    Z = np.asarray(Z, dtype=np.float64)

    A, a, B, b = W

    A = np.asarray(A, dtype=np.float64)
    a = np.asarray(a, dtype=np.float64)
    B = np.asarray(B, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)

    if X.ndim != 2 or X.shape[0] != 6:
        raise ValueError("X must have shape (6, lx)")
    if Z.ndim != 2 or Z.shape[0] != 10:
        raise ValueError("Z must have shape (10, lz)")
    if A.shape != (4, 6):
        raise ValueError("A must have shape (4, 6)")
    if a.shape != (4,):
        raise ValueError("a must have shape (4,)")
    if B.shape != (4, 10):
        raise ValueError("B must have shape (4, 10)")
    if b.shape != (4,):
        raise ValueError("b must have shape (4,)")
    P = A @ X + a[:, np.newaxis]
    R = B @ Z + b[:, np.newaxis]
    S = (R.T @ P) / np.sqrt(4)

    return S

class TestPairScore(unittest.TestCase):

    def setUp(self):
        # Create sample inputs
        rng = np.random.default_rng(42)

        self.X = rng.random((6, 3))
        self.Z = rng.random((10, 5))

        self.A = rng.random((4, 6))
        self.a = rng.random(4)

        self.B = rng.random((4, 10))
        self.b = rng.random(4)

        self.W = (self.A, self.a, self.B, self.b)

    # Test 1: Check output shape and formula
    def test_pair_score(self):

        S = pair_score(self.X, self.Z, self.W)

        # Reference calculation
        P = self.A @ self.X + self.a[:, None]
        R = self.B @ self.Z + self.b[:, None]

        expected = (R.T @ P) / np.sqrt(4)

        self.assertEqual(S.shape, (5, 3))

        np.testing.assert_allclose(S, expected)

    # Test 2: Check effect of changing b
    def test_delta(self):

        delta = np.array([1, 2, 3, 4], dtype=float)

        S1 = pair_score(self.X, self.Z, self.W)

        new_W = (self.A, self.a, self.B, self.b + delta)

        S2 = pair_score(self.X, self.Z, new_W)

        # Expected change
        P = self.A @ self.X + self.a[:, None]

        expected_change = (
            np.ones((5, 1)) @ (delta @ P).reshape(1, 3)
        ) / np.sqrt(4)

        np.testing.assert_allclose(
            S2 - S1, expected_change
        )


if __name__ == "__main__":
    unittest.main()
