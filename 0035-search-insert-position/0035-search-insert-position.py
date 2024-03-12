class Solution:
    def searchInsert(self, nums, target):
        counter = 0
        nums.sort()
        if target in nums:
            return nums.index(target)
        elif target > max(nums):
            return len(nums)
        elif target < min(nums):
            return 0
        else:
            for i in nums:
                if i < target:
                    counter += 1
            return counter