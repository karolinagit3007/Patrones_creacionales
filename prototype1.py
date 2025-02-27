import copy


class Prototype:
    def __init__(self, data):
        self.data = data

    def clone(self):
        return copy.deepcopy(self)
    
original = Prototype([1, 2, 3])
clone = original.clone()


print(original.data) 
print(clone.data)

clone.data.append(4)

print(original.data) 
print(clone.data)