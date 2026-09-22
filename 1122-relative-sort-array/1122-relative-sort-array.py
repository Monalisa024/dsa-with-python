class Solution:
    def relativeSortArray(self, arr1, arr2):
        ans = []

        for i in arr2:
            for j in arr1:
                if i == j:
                    ans.append(j)

        for i in sorted(arr1):
            if i not in arr2:
                ans.append(i)
        return ans
 
        