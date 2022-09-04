# Runtime: 42 ms, faster than 97.62% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 14.7 MB, less than 42.02% of Python3 online submissions for Valid Palindrome.
# ''.join(filter(str.isalnum, s)).lower()

class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = ''.join(filter(str.isalnum, s)).lower()
        length = len(pal)
        for i,n in enumerate(pal[:int(length/2)]):
            if n == pal[-i-1]:
                continue
            else:
                return False
        return True