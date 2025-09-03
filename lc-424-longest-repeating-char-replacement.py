# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length

def characterReplacement(s: str, k: int) -> int:
    longest = 0
    counts = [0]*26
    l=0
    for r in range (len(s)):
        counts[ord(s[r])-ord('A')] += 1
        while (r-l+1)-max(counts) > k:
            #print (ord(s[l])-ord('A'))
            counts[ord(s[l])-ord('A')] -= 1
            l+=1
        longest = max(longest,r-l+1)
    return longest

print (characterReplacement(s="AABABBA",k=1)==4)