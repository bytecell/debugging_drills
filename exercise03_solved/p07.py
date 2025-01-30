import pdb

def append_to_list(value, lst=None):
    if lst == None:
        return [value]
    lst.append(value)
    return lst

print(append_to_list(1)) 
print(append_to_list(2)) 
