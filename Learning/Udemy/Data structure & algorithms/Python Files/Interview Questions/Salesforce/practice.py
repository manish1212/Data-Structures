# import math
# import heapq
# '''
# # Given an array of ints find the largest value
# def largest(arr):
#     max_val = -math.inf
#     print(max_val)

#     for i in range(len(arr)):
#         if arr[i]>max_val:
#             max_val = arr[i]
#     return max_val
# input_array = [1,2,3,40,5,6,7,8,10]
# print(largest(input_array))
# '''

# # Given an array of ints and an int k, find the k-th largest value
# def kthlargest(arr, k):
#     max_arr = []
#     heapq.heapify(max_arr)

#     for i in range(len(arr)):
#         heapq.heappush(max_arr,arr[i])
#         if len(max_arr)>k:
#             heapq.heappop(max_arr)
#     return max_arr[0]

#     # return heapq.nlargest(k,arr)[k-1]

# input_array = [1,2,3,40,5,6,7,8,10]
# print(kthlargest(input_array,4))

