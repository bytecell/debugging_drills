import pdb

class MyClass:
    def __init__(self, name, values=[]): 
        self.name = name
        self.values = values

    def add_value(self, value):
        self.values.append(value)

obj1 = MyClass('obj1')
obj1.add_value(10)

obj2 = MyClass('obj2')
obj2.add_value(20)

print(obj1.values)  
print(obj2.values)

