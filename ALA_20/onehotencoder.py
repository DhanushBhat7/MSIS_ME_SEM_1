import numpy as np
import unittest

def onehot(labels,n_classes):
    one_hot = np.zeros((len(labels),n_classes))

    one_hot[np.arange(len(labels)),labels] = 1

    return one_hot

class TestOneHot(unittest.TestCase):
    def setUp(self):
        self.x = np.asarray([0,1,2,1,0],dtype = int)

    def test(self):
        output = onehot(self.x,3)
        expected = [[1,0,0],[0,1,0],[0,0,1],[0,1,0],[1,0,0]]

        np.testing.assert_equal(output,expected)

if __name__ == "main":
    unittest.main()