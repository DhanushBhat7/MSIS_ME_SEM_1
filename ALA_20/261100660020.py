
import numpy as np
import unittest

""" QUESTION 1: Implement PAIRSCORE (15 marks) """


def pair_score(X, Z, W):

    # Convert all inputs to float64
    X = np.asarray(X, dtype=np.float64)
    Z = np.asarray(Z, dtype=np.float64)

    # Extract the four parameters from W
    if not isinstance(W, tuple) or len(W) != 4:
        raise ValueError("W must be a tuple (A, a, B, b)")

    A, a, B, b = W

    A = np.asarray(A, dtype=np.float64)
    a = np.asarray(a, dtype=np.float64)
    B = np.asarray(B, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)

    """ QUESTION 1(a): Check shapes """

    # X must have 6 rows and a positive number of columns
    if X.ndim != 2 or X.shape[0] != 6 or X.shape[1] == 0:
        raise ValueError("Invalid shape of X")

    # Z must have 10 rows and a positive number of columns
    if Z.ndim != 2 or Z.shape[0] != 10 or Z.shape[1] == 0:
        raise ValueError("Invalid shape of Z")

    # Check the shapes of all parameters
    if A.shape != (4, 6):
        raise ValueError("Invalid shape of A")

    if a.shape != (4,):
        raise ValueError("Invalid shape of a")

    if B.shape != (4, 10):
        raise ValueError("Invalid shape of B")

    if b.shape != (4,):
        raise ValueError("Invalid shape of b")

    """
     QUESTION 1(b): Calculate P 
     P = AX + a * ones(1, lx)
    """
    P = A @ X + a[:, None]

    """
    QUESTION 1(c): Calculate R 
    R = BZ + b * ones(1, lz)
    """
    R = B @ Z + b[:, None]

    """
    QUESTION 1(d): Calculate and return S 
    S = R.T @ P / sqrt(dh), where dh = 4
    """

    S = R.T @ P / np.sqrt(4)

    return S


""" QUESTION 2(c): Unit tests """

class TestPairScore(unittest.TestCase):

    def setUp(self):

        # Choose lx = 3 and lz = 2
        self.X = np.ones((6, 3), dtype=np.float64)
        self.Z = np.ones((10, 2), dtype=np.float64)

        self.A = np.ones((4, 6), dtype=np.float64)
        self.a = np.ones(4, dtype=np.float64)

        self.B = np.ones((4, 10), dtype=np.float64)
        self.b = np.ones(4, dtype=np.float64)

        self.W = (self.A, self.a, self.B, self.b)

 
    """ Test for Question 2(a): Output shape """


    def test_output_shape(self):
        """Check that S has shape (lz, lx)."""

        S = pair_score(self.X, self.Z, self.W)

        self.assertEqual(S.shape, (2, 3))


    # Test for Question 2(a): Correct numerical result

    def test_correct_values(self):
        """Check the score values using a known example."""

        S = pair_score(self.X, self.Z, self.W)

        # P contains 7 and R contains 11.
        # Each score = (4 * 11 * 7) / 2 = 154.
        expected = np.full((2, 3), 154.0, dtype=np.float64)

        np.testing.assert_allclose(
            S, expected, rtol=1e-7, atol=1e-8
        )

    # Test for Question 1(a): Invalid input shape

    def test_invalid_X(self):
        """Check that invalid X raises ValueError."""

        X = np.ones((5, 3), dtype=np.float64)

        with self.assertRaises(ValueError):
            pair_score(X, self.Z, self.W)


    # Test for Question 1(a): Invalid parameter shape

    def test_invalid_A(self):
        """Check that invalid A raises ValueError."""

        A = np.ones((4, 5), dtype=np.float64)
        W = (A, self.a, self.B, self.b)

        with self.assertRaises(ValueError):
            pair_score(self.X, self.Z, W)


    # Test for Question 2(b): Change in b

    def test_bias_change(self):
        """Check the formula for the change in S."""

        # Change b to b + delta
        delta = np.array([1, 0, 0, 0], dtype=np.float64)

        S1 = pair_score(self.X, self.Z, self.W)

        new_b = self.b + delta
        new_W = (self.A, self.a, self.B, new_b)

        S2 = pair_score(self.X, self.Z, new_W)

        # Actual change in S
        change = S2 - S1

        # Expected change = ones(lz, 1) @ (delta.T @ P / 2)
        P = self.A @ self.X + self.a[:, None]

        row = (delta @ P / 2)[None, :]

        expected = np.ones(
            (self.Z.shape[1], 1), dtype=np.float64
        ) @ row

        # Compare using floating-point tolerance
        np.testing.assert_allclose(
            change, expected, rtol=1e-7, atol=1e-8
        )

        # Every row of the change matrix must be identical
        np.testing.assert_allclose(
            change[0], change[1], rtol=1e-7, atol=1e-8
        )


# Run all tests and display their results
if __name__ == "__main__":
    unittest.main()
