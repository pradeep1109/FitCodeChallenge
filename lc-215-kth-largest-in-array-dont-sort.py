#Given an integer array nums and an integer k, return the kth largest element in the array.
#
#Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
#Can you solve it without sorting?
#
# 
#
#Example 1:
#
#Input: nums = [3,2,1,5,6,4], k = 2
#Output: 5
#Example 2:
#
#Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
#Output: 4
# 
#
#Constraints:
#
#1 <= k <= nums.length <= 10^5
#-10^4 <= nums[i] <= 10^4

import heapq

def my_soln (nums,k):
    my_heap = []

    for i in nums:
        heapq.heappush(my_heap,-1*i)

    for i in range(k):
        out = -1*heapq.heappop(my_heap)
   
    return out

print (my_soln(nums = [3,2,1,5,6,4], k = 2) == 5)

print (my_soln(nums = [3,2,3,1,2,4,5,5,6], k = 4) == 4)

print (my_soln(nums = [3,2,3,1,2,4,5,5,6], k = len([3,2,3,1,2,4,5,5,6])) == 1)

print (my_soln(nums = [3,2,3,1,2,4,5,5,6], k = 1) == 6)
