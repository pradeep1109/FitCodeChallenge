# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# Example 2:

# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
# Example 3:

# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.
# 1 <= k <= s.length

def sliding_window (s,k):
    '''
    get first window for vowel count
    move window, if first element is vowel, reduce count by 1, if last element is vowel increase count by 1
    update return count
    '''
    VOWELS=['a','e','i','o','u']
    cur_count = 0
    for c in s[:k]:
        if c in VOWELS:
            cur_count += 1

    max_count=cur_count

    #print ("max count at start is %s"%max_count)
    #print ("cur_window at start is %s"%s[:k])

    for i in range (1,len(s)-k+1):
        print (s[i-1:i+k])
        print ("current window is %s"%s[i:i+k])
        print (s[i-1],s[i+k-1])
        if s[i-1] in VOWELS:
            # 0, 3
            cur_count-=1
        if s[i+k-1] in VOWELS:
            cur_count+=1
        print ("cur_count after checking is %s"%cur_count)
        max_count = max(max_count,cur_count)

    return max_count

print(sliding_window("weallloveyou",7))