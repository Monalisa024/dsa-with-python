class Solution:
    def isPossibleToSplit(self, nums):
        for num in set(nums):
            if nums.count(num)>2:
                return False
        return True
        