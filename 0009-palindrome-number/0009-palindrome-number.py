class Solution:
    def isPalindrome(self, x):
        l = []
        for i in str(x):
            l.append(i)
            a = list(reversed(l))
        return l == a