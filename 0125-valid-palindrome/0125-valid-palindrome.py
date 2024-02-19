class Solution:
    def isPalindrome(self, s) :
        punctuation = '''`~"'!@#$%^[]&*()_+|}-_=+\{/?.:;>,<'''
        a = ''
        s = s.lower().split()
        for i in s:
            a += i
        for i in a:
            if i in punctuation:
                a = a.replace(i, '')
        return a == a[::-1]