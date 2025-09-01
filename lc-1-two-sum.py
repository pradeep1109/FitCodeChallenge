# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

def two_sum (numbers,target):
    dict1 = {}
    for idx,val in enumerate (numbers):
        dict1[val] = idx 
    print (dict1)
    for idx,val in enumerate (numbers):
        if target-val in dict1 and dict1[target-val]!=idx:
            #print ([min(idx,),max(idx,pair_idx)])
            return [min(idx,dict1[target-val]),max(idx,dict1[target-val])]

print (two_sum([3,4,5,6],7)==[0,1])