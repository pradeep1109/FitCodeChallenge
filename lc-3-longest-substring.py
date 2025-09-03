# Given a string s, find the length of the longest substring without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

def my_soln (s):
    charSet = set()
    l=res=0
    for r in range(len(s)):
        print (charSet)
        while s[r] in charSet:
            charSet.remove(s[l])
            l+=1
        res= max(res,r-l+1)
        charSet.add(s[r])
    return res

print (my_soln("bbbbb")==1)
print (my_soln("abcabcbb")==3)