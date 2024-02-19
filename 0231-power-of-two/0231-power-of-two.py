class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n > 0:
            import math
            a = int(math.log2(n))
            return 2**a == n
        else:
            return False