import pdb
import math

a = 0.1 + 0.2
if math.isclose(a, 0.3, rel_tol=1e-9):
    print("Same")
else:
    print("Different")
