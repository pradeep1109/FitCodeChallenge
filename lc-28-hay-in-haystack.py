# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

# Constraints:

# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters

def working_soln (haystack,needle):
    if haystack == needle:
        return 0
    for i in range (len(haystack)-len(needle)+1):
        #print (haystack[i:i+len(needle)])
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

def my_soln (haystack,needle):
    needle_copy = needle
    idx = -1
    for i in range(len(haystack)):
        #print (haystack[i]," ", needle_copy)
        if needle_copy and haystack[i] == needle_copy[0]:
            if needle_copy == needle:
                idx = i
            needle_copy = needle_copy[1:]
        elif haystack[i] != needle_copy[0]:
            idx = -1
            needle_copy = needle
        if not needle_copy:
            break
    #print (needle_copy)
    if not needle_copy:
        return idx
    else:
        return -1

state = "meh"
soln = my_soln if state == "happy" else working_soln

print (soln (haystack = "sadbutsad",needle = "sad")==0)
print (soln (haystack = "leetcode",needle = "leeto")==-1)
print (soln (haystack='aaa',needle='aaaa')==-1)
print (soln (haystack="mississippi",needle='issip')==4)
print (soln (haystack="hello",needle="ll")==2)
print (soln (haystack="a",needle="a")==0)
print (soln (haystack="abc",needle="")==-1)
