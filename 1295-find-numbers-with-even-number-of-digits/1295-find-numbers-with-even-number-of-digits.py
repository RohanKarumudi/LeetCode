class Solution:
    def findNumbers(self, nums):
        l = []
        for i in nums:
            i = str(i)
            if len(i) % 2 == 0:
                l.append(i)
        return len(l)