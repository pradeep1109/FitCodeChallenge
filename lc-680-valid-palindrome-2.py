#Given a string s, return true if the s can be palindrome after deleting at most one character from it.
#
# 
#
#Example 1:
#
#Input: s = "aba"
#Output: true
#Example 2:
#
#Input: s = "abca"
#Output: true
#Explanation: You could delete the character 'c'.
#Example 3:
#
#Input: s = "abc"
#Output: false
# 
#
#Constraints:
#
#1 <= s.length <= 10^5
#s consists of lowercase English letters.

def returnValidPalindrome(s):
    return s==s[::-1]

def my_soln(s):
    l = 0
    r = len(s)-1

    allowed = 1

    while l < r:
        if s[l] != s[r] and allowed:
            allowed -= 1
            return returnValidPalindrome(s[l+1:r+1]) or returnValidPalindrome(s[l:r])
        elif not allowed:
            return False
        l+=1
        r-=1
    return True

print (my_soln(s="aba") == True)

print (my_soln(s="abca") == True)

print (my_soln(s="abc") == True)
