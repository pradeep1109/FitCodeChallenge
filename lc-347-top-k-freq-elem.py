# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2

# Output: [1,2]

# Example 2:

# Input: nums = [1], k = 1

# Output: [1]

# Example 3:

# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

# Output: [1,2]

 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
 

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

def my_soln (nums,k):
    num_dict = {}
    for num in nums:
        num_dict[num] = 1+ num_dict.get(num,0)
    print (num_dict)
    freq = [[] for i in range(len(nums)+1)]
    print (freq)
    for num,val in num_dict.items():
        print (num,val)
        print (freq[val])
        freq[val].append(num)
        print (freq[val])
    print (freq)
    res = []
    for idx in range (len(freq)-1,0,-1):
         if freq[idx]:
             print (freq[idx])
             for i in freq[idx]:
                res.append(i)
                print (res)
                if len(res) == k:
                    return res
        

    # res_list = []
    # print(num_dict)
    # for num in nums:
    #     if num_dict[num] == k:
    #         res_list.append(num)
    # print (res_list)
    # return [res_list]

print (my_soln(nums = [1,2,1,2,1,2,3,1,3,2], k = 2) == [1,2])