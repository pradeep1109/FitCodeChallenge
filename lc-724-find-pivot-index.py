# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is
#  equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are no elements
#  to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.

# Example 1:

# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11
# Example 2:

# Input: nums = [1,2,3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.
# Example 3:

# Input: nums = [2,1,-1]
# Output: 0
# Explanation:
# The pivot index is 0.
# Left sum = 0 (no elements to the left of index 0)
# Right sum = nums[1] + nums[2] = 1 + -1 = 0
 

# Constraints:

# 1 <= nums.length <= 104
# -1000 <= nums[i] <= 1000

def my_soln (nums):
    #print ("top, nums is %s"%nums)
    '''
    for each index, find sum of all elements left and sum of all elements right
    if idx = left corner, left_sum is 0, right corner, right_sum is 0
    can this be done in O(n)
    '''
    left_sum=right_sum=0
    for idx in range (len(nums)):
        left_sum = 0 if not idx else sum(nums[:idx])
        #print ("left_sum is %s, for %s"%(left_sum,nums[:idx]))
        right_sum = 0 if idx == len(nums)-1 else sum(nums[idx+1:])
        #print ("right_sum is %s, for %s"%(right_sum,nums[idx+1:]))
        if left_sum == right_sum:
            return idx
    return -1

for nums in [[1,7,3,6,5,6],[1,2,3],[2,1,-1]]:
    print (my_soln (nums=nums))

