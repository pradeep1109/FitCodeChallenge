'''
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
'''

def working_soln(nums):
    '''
    consider 2 infinite numbers
    go through the list
    if current num is less than num i, then update num i
    else, if current num is less than num j, then update num j
    by this if condition, num i < num j always, since that ll get updated first
    num i and num j are set in such a way that num i < num j
    from now on, num i will get updated only if num <= num i
    until last element
        if there is a num > num i, num j will get updated if its <= num j
        if there is a num thats greater than num j that means we reached the triplet req
    if this keeps getting updated till the last element
        => there is no num sequence that satisfies the condition i<j<k, num[i]<num[j]<num[k]
    '''
    num_i, num_j = (float('inf'),float('inf'))
    for num in nums:
        if num <= num_i:
            num_i = num
        elif num <= num_j:
            num_j = num
        else:
            return True        
    return False

def my_soln (nums):
    '''
    start at idx 0, consider that the biggest number
    then start moving down the line, if any item is bigger than current big number, update
    keep moving until you encounter one more big number, if you do, return true
    '''
    biggest = nums[0]
    res_list = [nums[0]]
    for i in range(len(nums)):
        if nums[i] > res_list[-1]:
            res_list.append(nums[i])
            print (res_list)
            if len(res_list) == 3:
                return True
        if (nums[i]) < res_list[-1]:
            res_list = [nums[i]]
    return False


print (working_soln([20,100,10,12,5,13]))