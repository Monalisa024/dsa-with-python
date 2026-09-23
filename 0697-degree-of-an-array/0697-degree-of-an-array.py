class Solution:
    def findShortestSubArray(self, nums):
        count = {}
        first = {}
        last = {}

        for i in range(len(nums)):
            num = nums[i]

            if num not in count:
                count[num] = 0
                first[num] = i

            count[num] += 1
            last[num] = i

        degree = max(count.values())
        ans = len(nums)

        for num in count:
            if count[num] == degree:
                ans = min(ans, last[num] - first[num] + 1)

        return ans

        