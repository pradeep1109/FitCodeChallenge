# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

# Example 1:

# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
# Example 2:

# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
# Example 3:

# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.

def var_sliding_window_mylogic (nums,):
    max_w = l = flip = cur_w= 0
    allowed_del = 1

    #print ("top: nums is %s"%nums)

    #if 0 not in nums:
    #    return 0

    for r in range (len(nums)):
        print ("inside for loop: nums[r] is %s, r is %s, l is %s, allowed_del is %s, flip is %s, max_w is %s, cur_w is %s"%(nums[r],r,l,allowed_del,flip,max_w,cur_w))
        if not nums[r]:
            if allowed_del:
                # include zero, since it allowed
                allowed_del-=1 # decrement since its no longer allowed for this window
                flip = r # at this r we flipped an element
                #continue # increment window
            # elif not nums[l]:
            #      # allowed_del is 0, since first element in window was 0, we need to remove that from the window and include this
            #      # cant reclaim allowed_del
            #      cur_w = r-l
            #      max_w = max(cur_w,max_w)
            #      l = flip+1
            #      flip = r
            #      #continue
            else:
                # this means the first element in the window was a 1, and some element in the middle got changed to 0
                # the window is done
                # we need to move l in such a way flipping this 0 will give a longer subarray than the previous
                # which means, move the l to earlier flip+1
                # make note of max window
                #cur_w = r-l-1
                #max_w = max(cur_w,max_w)
                l = flip+1
                flip=r
                print ("updating window: r is %s, l is %s, max_w is %s, cur_w is %s"%(r,l,max_w,cur_w))
        else:
            # current num is a 1
            # continue incrementing window size
            pass
        #cur_w = r-l
    return max(max_w,r-l-1)

def sliding_window(nums):
    num_zero = 1 # allowed dels is 1
    l=0 # left pointer

    for r in range (len(nums)): # move right pointer
        num_zero -= nums[r] == 0 # if cur element is a zero, decrement allowed deletes by 1

        if num_zero < 0: # if current window contains more than 1 zero (ie, num_zero becomes -1)
            num_zero += nums[l] == 0 # if nums[l] was zero, then within the window 2 deletes were done
                                     # if window size is reduced, allowed deletes becomes 0
                                     # if not, keep that at -1, until we know where the other delete happened, this is cause we increment l
                                     # now that becomes the new window
            l+=1                     # window is moved by 1
    return r-l

#print(var_sliding_window_mylogic([0,1,1,1,0,1,1,0,1]))
#print(var_sliding_window_mylogic([1,1,1,0,1]))
#print(var_sliding_window_mylogic([1,1,1]))

#print(sliding_window([0,1,1,1,0,1,1,0,1]))
print (sliding_window([1,0,0,1,1,0,1,0,1,1,0,1,0,1,0,1,0]))
#print(var_sliding_window_mylogic([1,1,1,0,1]))
#print(var_sliding_window_mylogic([1,1,1]))
