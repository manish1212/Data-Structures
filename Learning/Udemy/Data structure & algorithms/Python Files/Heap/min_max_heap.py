# heap by default min heap
'''
heapify() - to CONVERT in to heap
heappush(heap, element) - to PUSH in heap
heappop(heap) - REMOVE & RETURN smallest element
'''

import heapq

'''Min heap (default)'''
min_heap = []
heapq.heapify(min_heap)
heapq.heappush(min_heap,10)
heapq.heappush(min_heap,50)
heapq.heappush(min_heap,30)
heapq.heappush(min_heap,400)

print('min heap tree', min_heap)
print('min heap value', min_heap[0])
print('removed min', heapq.heappop(min_heap))
print('min heap tree', min_heap)

print(heapq.nlargest(2,min_heap))
print(heapq.nsmallest(2,min_heap))

print('-------')

'''Max heap'''
heap = []
heapq.heapify(heap)

# multiply by -1 to make a max heap
heapq.heappush(heap,-1*10)
heapq.heappush(heap,-1*50)
heapq.heappush(heap,-1*30)
heapq.heappush(heap,-1*400)

# while retrieving multiple by -1
print('max heap tree', heap)
print('max heap value', str(-1*heap[0]))
print('removed max', heapq.heappop(heap))
print('max heap tree', heap)


'''Notes for reference'''
#  0 1 2 3 4 
#    i
# Arr[0] - root
# for Arr[i]
# Arr[(i-1)/2] Returns the parent node. 0
# Arr[(2*i)+1] Returns the left child node. 3
# Arr[(2*i)+2] Returns the right child node. 4