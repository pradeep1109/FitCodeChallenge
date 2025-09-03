# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 

# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

def mergeSort (nums):
    # reduce to base case, single elems 
    # merge elems, single or in arr --> this becomes a merge sorted arrays problem
    if len(nums) > 1:
        left_arr = nums[:len(nums)//2]
        right_arr = nums[len(nums)//2:]
        mergeSort(left_arr)
        mergeSort(right_arr)
        i=j=k=0
        #print (nums)
        #print (left_arr,right_arr)
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] > right_arr[j]:
                nums[k] = right_arr[j]
                j+=1
            else:
                nums[k] = left_arr[i]
                i+=1
            k+=1
            #print (nums,k)
        while i < len(left_arr):
            nums[k] = left_arr[i]
            i+=1
            k+=1
        while j < len(right_arr):
            nums[k] = right_arr[j]
            j+=1
            k+=1
    return nums

def retOrd(l1):
    #print (l1)
    #l1 = mergeSort(l1)
    l2 = [str(_i) for _i in l1]
    return ("%s_%s_%s"%(l2[0],l2[1],l2[2]))

def threeSum (nums):
    nums = mergeSort(nums)
    #print (nums)
    res = []
    for pivot_idx in range (len(nums)-2): # stop at len-2, if last 3 elements are the triplet
        l = pivot_idx+1
        r = len(nums)-1
        if pivot_idx >0 and nums[pivot_idx] == nums[pivot_idx-1]:
            continue # remove duplicates
        #print (nums[pivot_idx])
#        diff = 0-nums[pivot_idx]
#        print (diff)
        while l<r and l<len(nums)-1 and r<len(nums):
            #print (nums,l,r,pivot_idx)
            sum = nums[l]+nums[r]+nums[pivot_idx]
#            print (nums[l],nums[r])
#            print (nums[r]+nums[l]-diff)
            if not sum:
                res.append([nums[pivot_idx],nums[l],nums[r]])
                l+=1
                continue
            elif sum > 0:
                r-=1
            else:
                l+=1
    #print (res)
    dict1= {}
    for _r in res:
        rord = retOrd(mergeSort(_r))
        #print (rord)
        if rord not in dict1:
            dict1[rord]=_r
    
    #print ([_r for _r in dict1.values()])
    return [_r for _r in dict1.values()]

    #print (res)
    #return res

print (threeSum(nums=[-1,0,1,2,-1,-4])==[[-1,-1,2],[-1,0,1]])
print (threeSum(nums=[0,0,0])==[[0,0,0]])
print (threeSum(nums=[0,1,1])==[])
print (threeSum([-2,0,1,1,2])==[[-2,0,2],[-2,1,1]])