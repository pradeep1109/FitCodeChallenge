# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1
 

# Constraints:

# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4

def maxArea(heights: list[int]) -> int:
    # area = (ptr2-ptr1)*min(heights[ptr1:ptr2])
    # two pointers
    #   condition to move pointer -area will shrink if we 
    #       move the larger height
    l,r,area = 0,len(heights)-1,0
    while l<r:
        #print (area,abs(l-r)*min(heights[l],heights[r]))
        area = max(area,abs(l-r)*min(heights[l],heights[r]))
        if heights[l]<heights[r]:
            l+=1
        else:
            r-=1
    return area


print (maxArea([1,8,6,2,5,4,8,3,7])==49)