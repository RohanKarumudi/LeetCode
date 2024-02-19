class Solution:
    def lengthOfLastWord(self, str):
        str = str.split()
        return len(str[-1])