# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars.
#  Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.

# You must write an algorithm that uses only constant extra space.

# Example 1:

# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
# Example 2:

# Input: chars = ["a"]
# Output: Return 1, and the first character of the input array should be: ["a"]
# Explanation: The only group is "a", which remains uncompressed since it's a single character.
# Example 3:

# Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
# Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
 

# Constraints:

# 1 <= chars.length <= 2000
# chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.

def bruteforce (chars):
    # move through array
    # add element to compressed string 
    #     when you encounter consecutive characters, start counter
    #     when character is different reset counter and append current result to compressed string
    s=[]
    print (len(chars))
    j=1
    s.append(chars[0])
    while j < len(chars):
        #assumption is s already has the next character to check in it, at j=1, this is accomplished by the previous line
        char_count = 0
        char = chars[j] # chars aa, s a
        print ("char is %s"%char)
        print ("top of loop s is %s"%s)
        #print ("top of loop, chars is %s"%chars)
        print ("just above consecutive check while loop, j is %s"%j)
        while len(chars) > j and s[-1] == char: # encountered duplicate char
            import pdb
            try:
                char_count+=1
                print ("inside consecutive check j is %s, char is %s, char_count is %s"%(j,chars[j],char_count))
                char = chars[j]
                j+=1
                _j=j
            except:
                #pdb.set_trace ()
                raise UnboundLocalError
        if char_count:
            print ("for %s char_count is %s"%(chars[j-1],char_count))
            s += [i for i in str(char_count)]
        print ("after consecutive check s is %s"%s) # at this point, add new char based on initial assumption
        print (s)
        if s[-1] != char:
            s += char
        print ("end of loop, s is %s, j is %s, chars[j] is %s"%(s,j,chars[j]))
        j+=1
    print (s[:-1])
    return (chars+s[:-1])

def _2ptrs (chars):
    '''
    condition is to use the same array for insertion
    move through the list using i
    at current i if you see i+1 as 
    '''
    if len(chars) == 1:
        return 1
    index,i = (0,0)
    while i < len(chars):
        j = i
        while j < len(chars) and chars[j] == chars[i]:
            j += 1
        chars [index] = chars[i]
        index+=1
        if j-i > 1:
            for k in str(j-i):
                chars[index] = k
                index+=1
        i=j
    return index

print(_2ptrs (["a","a","b","b","c","c","c"]))