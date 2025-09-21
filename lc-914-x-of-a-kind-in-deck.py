#You are given an integer array deck where deck[i] represents the number written on the ith card.
#
#Partition the cards into one or more groups such that:
#
#Each group has exactly x cards where x > 1, and
#All the cards in one group have the same integer written on them.
#Return true if such partition is possible, or false otherwise.
#
# 
#
#Example 1:
#
#Input: deck = [1,2,3,4,4,3,2,1]
#Output: true
#Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
#Example 2:
#
#Input: deck = [1,1,1,2,2,2,3,3]
#Output: false
#Explanation: No possible partition.
# 
#
#Constraints:
#
#1 <= deck.length <= 10^4
#0 <= deck[i] < 10^4

import math

def my_soln (deck):
    hash_map = {}
    for i in deck:
        hash_map[i] = 1+hash_map.get(i,0)

    cur_gcd = 0

    for count in hash_map.values ():
        cur_gcd = math.gcd(count,cur_gcd)

    return cur_gcd > 1

print (my_soln(deck=[1,2,3,4,4,3,2,1])==True)

print (my_soln(deck=[1,1,1,2,2,2,3,3])==False)
