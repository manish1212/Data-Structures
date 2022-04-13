class HashTable:
    def __init__(self, size):
        """
		Create an array(self.mydict) with a bucket size - which is derived from the load factor.
		The Load factor is a measure that decides when to increase the HashMap capacity 
        to maintain the get() and put() operation complexity of O(1).
		The default load factor of HashMap is 0.75f (75% of the map size).
		Load Factor = (n/k)
		where n is the number of max number of elements that can be stored in dict
		k is the bucket size
		Optimal Load factor is around (2/3) such that the effect of hash collisions is minimum 
		"""
        self.bucket = size
        self.data = [[] for i in range(self.bucket)]
    
    def __str__(self):
        return str(self.__dict__)

    def hash(self,key):
        # return randrange(self.bucket)
        return len(key) % len(self.data)
    
    def put(self, key, value):
        address = self.hash(key)
        if not self.data[address]:
            self.data[address] = []
        self.data[address].append([key, value])
        return self.data

    def get(self, key):
        address = self.hash(key)
        currentBucket = self.data[address]
        
        if currentBucket:
            for i in range(len(currentBucket)):
                if currentBucket[i][0] == key:
                    return currentBucket[i]
        return 'No Value found'
    
    def keys(self):
        keyArrays = []
        for i in range(len(self.data)):
            currentBucket=self.data[i]
            if currentBucket:
                if(len(currentBucket)>1):
                    for j in range(len(currentBucket)):
                        collisionBucket = currentBucket[j]
                        if collisionBucket:
                            keyArrays.append(collisionBucket[0])
                else:
                    keyArrays.append(currentBucket[0][0])
        return keyArrays  

    def delete(self, key):
        address = self.hash(key)
        currentBucket = self.data[address]
        if currentBucket:
            if len(currentBucket)>1:
                for i in range(len(currentBucket)):
                    if currentBucket[i][0] == key:
                        currentBucket.pop(i)
                        return self.data
            currentBucket.pop(0)
        return self.data

h=HashTable(30)
h.put('a',10)
h.put('b',20)
print('adding',h.put('abc',20))
print('getting values',h.get('a'))
print("keys : ", h.keys())
print('deleted', h.delete('abc'))
print('after delete', h.get('c'))



d = {1:'a',2:'b',3:'c'}
print('manish', d.get(1) )