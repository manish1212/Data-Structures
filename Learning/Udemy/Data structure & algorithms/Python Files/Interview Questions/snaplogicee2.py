#interface RandomSet {
#    /** 
#    * Inserts a value to the set. Returns true if the set did not already contain the specified element. 
#    **/
#    boolean insert(int val);
#    /** 
#    * Removes a value from the set. Returns true if the set contains the specified element. 
#    **/
#    boolean remove(int val);
#    /** 
#    * Get a random element from the set. 
#    **/
#    int getRandom();
#}

import random

class DiffDsRandomSet():
    def __init__(self):
        self.arr = []
        self.dict = {}

    def insert(self, valueToInsert):
        if valueToInsert in self.dict:
            return None
        else: 
            self.arr.append(valueToInsert)
            self.dict[valueToInsert] = len(self.arr)-1
            return self.arr, self.dict

    def remove(self, valueToRemove):
        if valueToRemove in self.dict:
            position  = self.dict.pop(valueToRemove)
            last_item = self.arr.pop()
            if position != len(self.arr): # cant insert in arr at position higher than the length on line 36 # no need to insert when last element
                self.arr[position] = last_item
                self.dict[last_item]=position
        return self.arr, self.dict

    def getRandom(self):
        return random.choice(self.arr)


ds = DiffDsRandomSet()
print(ds.insert(1))
print(ds.insert(2))
print(ds.insert(3))
print(ds.insert(4))
# print(ds.insert(2))
# print(ds.getRandom())
print(ds.remove(4))


''' with the logic submitted to snaplogic '''
def randomSet(nums, toRemove):
    arr = nums
    dict = {}

    for i in range(len(arr)):
        dict[i] = arr[i]

    val_list = list(dict.values())

    # Swap the postions in dict
    toRemoveKey = val_list.index(toRemove)
    lastElementKey = len(val_list)-1
    lastElementValue = val_list[len(val_list)-1]
    dict[lastElementKey] = dict[toRemoveKey]
    dict[toRemoveKey] = lastElementValue

    # #pop last element
    temp = arr[toRemoveKey]
    arr[toRemoveKey] = arr[lastElementKey]
    arr[lastElementKey] = temp
    del arr[len(arr)-1]
    dict.popitem()
    return arr

nums = [11, 12, 13, 14, 15]
elementToRemove = 13

# print('final',randomSet(nums,elementToRemove))