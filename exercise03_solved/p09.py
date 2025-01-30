import pdb

def sum_recursive(n):
    if n == 0:
        return 0
    return n + sum_recursive(n)  

print(sum_recursive(5))
