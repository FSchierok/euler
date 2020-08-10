import numpy as np
from sympy.utilities.iterables import multiset_permutations

a=np.array([0,1,2,3,4,5,6,7,8,9])
p = list(multiset_permutations(a))
print(p[999999])
