# We are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array 
# represent their relative position in space.

# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right,
# negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode.
# If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

# Example 1:

# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
# Example 2:

# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.
# Example 3:

# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
 

# Constraints:

# 2 <= asteroids.length <= 10^4
# -1000 <= asteroids[i] <= 1000
# asteroids[i] != 0

def my_soln (asteroids):
    from collections import deque
    #stack = deque ()
    stack = []
    stack.append(asteroids[0])
    print ("asteroids is %s"%asteroids)
    for i in asteroids[1:]:
        print (stack,i)
        if not stack:
            stack.append(i)
            print (stack)
            continue
        if (stack[-1] *i) <0 and stack[-1] >0 and i <0:
            if abs(stack[-1])> abs(i) :
                print ("no need to add anything to stack")
                pass
            elif abs(stack[-1]) == abs(i):
                print ("pop existing item, dont add")
                stack.pop()
            else:
                print ("pop last element do recursive call")
                stack.pop ()
                stack.append(i)
                print (stack)
                stack = my_soln (stack)
        else:
            stack.append (i)
    #print ("returning %s"%stack)
    return list(stack)

options = {-1:{'in':[1,-1,-1,-2],'out':[-1,-2]},0:{'in':[1,-1,-2,-2],'out':[-2,-2]},1:{'in':[8,-8],'out':[]},2:{'in':[5,10,-5],'out':[5,10]},3:{'in':[10,2,-5],'out':[10]},4:{'in':[-2,-1,1,2],'out':[-2,-1,1,2]}}
for i in options:
    print (">> options[i] %s"%options[i])
    print (">> ",my_soln (asteroids=options[i]['in']) == options[i]['out'])
    #break