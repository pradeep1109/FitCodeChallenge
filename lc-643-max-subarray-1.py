# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000
 

# Constraints:

# n == nums.length
# 1 <= k <= n <= 105
# -104 <= nums[i] <= 104

'''
sliding window problem
contiguous subarray of length k
2 loops, 1 outer and 1 inner which goes to k - not needed, just use list comprehension
'''

def sliding_window(nums,k):
    cur_sum = max_sum = sum(nums[:k])
    for i in range(len(nums)-k):
        cur_sum = cur_sum-nums[i]+nums[i+k]
        max_sum = max (cur_sum,max_sum)
    return (max_sum/k)

print(sliding_window([1,12,-5,-6,50,3],4))