from typing import Self

class Vector:
    #recive list elements to initialise a vector 
    def __init__(self, src=None) -> Self:
        if src is None:
            self.elements=()
        else:
            elements = tuple(src)
            for x in elements:
                if not isinstance(x,(int,float)):
                    raise TypeError("scalar must be a number")
            self.elements=elements

    def scalar_mul(self,value):
        result=Vector(x*value for x in self.elements)
        return result

    def smul(self,val):
        el=list(self.elements)

        for i in range(len(el)):
            el[i]=val*el[i]

        result=Vector(el)
        return result
    
    def __repr__(self) -> str:
            return repr(self.elements)


    
if __name__ == "__main__":
    #z1 = Vec.zeros(10)
    v1 = Vector([1,2,3])
    print(v1)

    v2= v1.scalar_mul(3)
    print(v2)
    v3= v1.smul(3)
    print(v3)

        

        