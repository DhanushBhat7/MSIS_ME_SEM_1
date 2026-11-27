import numpy as np
import unittest

class vector:
    def __init__(self,x):
        self.x = np.array(x,dtype=np.float64)
        if self.x.ndim!=1:
            raise ValueError("input must 1D")
        if len(self.x)==0:
            raise ValueError("Vector cannot be empty")

    def mean(self):
        return np.sum(self.x)/len(self.x)

    def demean(self):
        return self.x-self.mean()

    def std(self):
        d = self.demean()
        return np.sqrt(np.sum(d**2)/len(self.x))

class Vectortest(unittest.TestCase):
    def setUp(self):
        self.v = vector([1,2,3,4,5])
        self.x = self.v.x

    def test_mean(self):
        emp_mean = self.v.mean()
        theor_mean = np.mean(self.x)
        self.assertAlmostEqual(emp_mean,theor_mean)

    def test_demean(self):
        emp_demean = self.v.demean()
        np.testing.assert_array_almost_equal(emp_demean,[-2,-1,0,1,2])

    def test_std(self):
        emp_std = self.v.std()
        theor_std = np.std(self.x)
        self.assertAlmostEqual(emp_std,theor_std)

    #optional ig
    def test_demeaned_mean(self):
        self.assertAlmostEqual(self.v.demean().mean(),0.0)

if __name__ == "__main__":
    unittest.main()
