# https://leetcode.com/problems/maximum-number-of-words-you-can-type/

# not a difficult question at all, we have to do is: 

# first use broken =  set() on the brokenLetters.
# init a count variable.
# run a for loop in text.split()
# if not in ( set(word) & broken ) then increase the count by 1.
# and return the count.


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        count = 0 

        for word in text.split():
            if not (set(word) & broken):
                count += 1

        return count
