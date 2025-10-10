#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
#
#Given a string s, return true if it is a palindrome, or false otherwise.
#
# 
#
#Example 1:
#
#Input: s = "A man, a plan, a canal: Panama"
#Output: true
#Explanation: "amanaplanacanalpanama" is a palindrome.
#Example 2:
#
#Input: s = "race a car"
#Output: false
#Explanation: "raceacar" is not a palindrome.
#Example 3:
#
#Input: s = " "
#Output: true
#Explanation: s is an empty string "" after removing non-alphanumeric characters.
#Since an empty string reads the same forward and backward, it is a palindrome.
# 
#
#Constraints:
#
#1 <= s.length <= 2 * 10^5
#s consists only of printable ASCII characters.

def isAlNum(c):
    _ord = ord(c)
#    print (c,_ord)
    return ord("A")<=_ord<=ord("Z") or ord("a")<=_ord<=ord("z") or ord("0")<=_ord<=ord("9")

def check(s):
    l=0
    r=len(s)-1
    while l<r:
        if not isAlNum(s[l]):
#            print ("isAlnum %s is %s"%(s[l],isAlNum(s[l])))
#            print (s[l])
            l+=1
            continue
        if not isAlNum(s[r]):
#            print (s[r])
            r-=1
            continue
#        print (s[l],s[r])
        if s[r].lower() != s[l].lower():
#            print ("return False")
            return False
        l+=1
        r-=1
        continue
    return True


print (isPalindrome("A man, a plan, a canal: Panama") ==True)

print (isPalindrome("race a car") ==False)

print (isPalindrome("abba")==True)

print (isPalindrome("talat")==True)

print (isPalindrome("         ")==True)
