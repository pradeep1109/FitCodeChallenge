# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
# The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
# The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int val = ...; // Value to remove
# int[] expectedNums = [...]; // The expected answer with correct length.
#                             // It is sorted with no values equaling val.

# int k = removeElement(nums, val); // Calls your implementation

# assert k == expectedNums.length;
# sort(nums, 0, k); // Sort the first k elements of nums
# for (int i = 0; i < actualLength; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

# Example 1:

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).
 

# Constraints:

# 0 <= nums.length <= 100
# 0 <= nums[i] <= 50
# 0 <= val <= 100

def my_soln (nums=[3,2,2,3],val=3):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow],nums[fast]=nums[fast],nums[slow]
            slow+=1
    return slow

def _my_soln (nums=[3,2,2,3],val=3):
    #print ("top, nums is %s, val is %s"%(nums,val))
    k=0
    for idx in range(len(nums)):
        if nums[idx] == val:
            k+=1
            nums[idx]='_'
    left = 0
    right = len(nums)-1
    #print (nums)
    while left < len(nums) and right > left+1:
        if nums[left] == '_':
            #print (nums,left,right)
            if nums[right] != '_':
                tmp = nums[right]
                nums[right]=nums[left]
                nums[left] = tmp
            while right and nums[right] == '_':
                right-=1
            # old soln
            # while right and nums[right] == '_':
            #     right-=1
            # #print (nums,left,right)
            # tmp = nums[right]
            # nums[right]=nums[left]
            # nums[left] = tmp
        left += 1
    #print (nums)
    return len(nums)-k

print (my_soln (nums=[3,2,2,3],val=3)==2)
print (my_soln (nums=[0,1,2,2,3,0,4,2],val=2)==5)
print (my_soln(nums=[3,3],val=3)==0)
print (my_soln(nums=[2,2,3],val=2)==1)
print (my_soln(nums=[4,5],val=4)==1)