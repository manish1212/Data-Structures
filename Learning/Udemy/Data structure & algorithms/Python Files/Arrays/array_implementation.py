class Array:
    def __init__(self):
        self.length = 0
        self.data = {}

#   def __str__(self):
#     return str(self.__dict__)

    def get(self, index):
        return self.data[index]
    
    def getElement(self, item):
        for i in range(0, self.length):
            val = self.data[i]
            if val == item:
                return i

    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.data

    def pop(self):
        del self.data[self.length-1]
        self.length -= 1
        return self.data

    def delete(self, index):
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        self.length -= 1
        return self.data

    def insert(self, index, value):

        if index >= self.length or index < 0:
            self.push(value)
            return self.data

        temp = self.data[index]
        for i in range(index, self.length-1):
            temp2 = self.data[i+1]
            self.data[i+1] = temp
            temp = temp2
            
        self.data[self.length] = temp
        self.data[index] = value
        self.length+=1
        return self.data

myArray = Array()
# myArray.push('a')
# myArray.get(0)
print(myArray.push('a'))
print(myArray.push('b'))
print(myArray.push('c'))
print(myArray.push('d'))
print(myArray.push('e'))
print(myArray.insert(1,'P'))
print("position",myArray.getElement('b'))

# print(myArray.pop())
# print(myArray.delete(1))
# print(myArray.get(1))
