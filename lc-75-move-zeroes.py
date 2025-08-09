import pdb

def bruteforce (nums):
    zero_count = 0
    #print (nums)
    idx=0
    while idx < len(nums):
        #print (nums)
        if not nums[idx]:
            nums.pop (idx)
            zero_count += 1
            #idx += 1
            continue
        idx += 1
            
    #for idx in range(0,len(nums)):
    #        if not nums[idx]:
    #            nums.pop(idx)
    #            zero_count += 1
    #print(nums)
    nums+=[0]*zero_count
    return nums

def _2ptrs (nums):
    # slow pointer, fast pointer
    # fast pointer moves through array, with for loop
    # slow pointer starts at 0, but moves to index+1 once swap is done based on condition
    # condition is if val at jth iteration is not a zero, swap with zero thats progressing through the list
    # the zero that progresses will change when new zero is encountered, for instance this list [0,1,3,2,0,1,3] here zero at idx 0 moves up
    #                           until it reaches idx 3, from there slow and fast counter move to the idx 3 and start the proces again
    slow = 0
    for fast in range (len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow+=1
    return nums

#print (bruteforce([0,1,0,3,12]))
#print (bruteforce([0, 0, 1]))
print (_2ptrs([0,1,0,3,12]))
print (_2ptrs([0, 0, 1]))