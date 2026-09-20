class Solution:
    def concatWithReverse(self, nums):
        list = []
        for i in range(len(nums)):
            list.append(nums[i])
        for i in range(len(nums)-1, -1, -1):
            list.append(nums[i])

        return list

        