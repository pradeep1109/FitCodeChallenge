# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

# Example 1:

# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
# Example 2:

# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessarily unique.
 
List = list

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort (arr,):
            if len(arr) > 1:
                left_arr = arr[:len(arr)//2]
                right_arr = arr[len(arr)//2:]
                mergeSort(left_arr) # at base case, this is noop
                mergeSort(right_arr) # at base case, this is noop
                i,j,k=0,0,0
                while i <len(left_arr) and j < len(right_arr):
                    if left_arr[i] <= right_arr[j]:
                        arr[k] = left_arr[i]
                        i+=1
                    else:
                        arr[k] = right_arr[j]
                        j+=1
                    k+=1
                while i < len(left_arr):
                    arr[k] = left_arr[i]
                    i+=1
                    k+=1 
                while j < len(right_arr):
                    arr[k] = right_arr[j]
                    j+=1
                    k+=1
            return arr
            
        return mergeSort(nums)

obj = Solution()
print (obj.sortArray([5,1,2,4,3]))