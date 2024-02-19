class Solution:
    def plusOne(self, digits):
        l = []
        a = ''
        for i in digits:
            a = a + str(i)
        a = int(a) + 1
        a = str(a)
        for i in a:
            l.append(i)
        n = (int(i) for i in l)
        return(n)