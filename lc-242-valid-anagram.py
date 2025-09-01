# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def my_soln (s: str, t: str) -> bool:
            if len(s) != len(t):
                return False
            count_s, count_t = {}, {}
            for i in range(len(s)):
                count_s[s[i]] = 1+count_s.get(s[i],0)
                count_t[t[i]] = 1+count_t.get(t[i],0)
            #print (count_s,count_t)
            for i in count_s:
                if count_s[i] != count_t.get(i,0):
                    return False
            return True
        return my_soln(s,t)

obj = Solution()
print (obj.isAnagram(s='anagram',t='nagaram') == True)
print (obj.isAnagram(s='jar',t='jam') == False)