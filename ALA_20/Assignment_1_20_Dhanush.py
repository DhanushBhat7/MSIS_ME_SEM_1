class Vector:
    def __init__(self, src=None):
        if src is None:
            self.elements=()
        else:
            elements = tuple(src)
            for x in elements:
                if not isinstance(x,(int,float)):
                    raise TypeError("scalar must be a number")
            self.elements=elements

    def mean(self):
        return sum(self.elements)/len(self.elements)

    def demean(self):
        mean_value = self.mean()
        return Vector([x - mean_value for x in self.elements])

    def std(self):
        deamenad = self.demean()
        squared = [x**2 for x in deamenad.elements]

        variance =  sum(squared)/len(squared)
        variance = variance ** 0.5

        return variance
    

v1 = Vector([2, 4, 6, 8, 10])
print(v1.elements)

mean = v1.mean()
print('the mean of the given vector: ',mean)

Demeaned_vector = v1.demean()
print('The Demeaned Vector of teh given vector is : ',Demeaned_vector.elements)

print ("The standard deviation: ",v1.std())



