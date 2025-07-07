import numpy as np
a=np.array([1,2,3,4])
b=np.array([4,3,2,4])
c=np.array([4,3,2,4])
s=np.equal(a,b)
p=np.array_equal(b,c)
print("Element wise equalitys", s)
print("Array wise equality", p)
