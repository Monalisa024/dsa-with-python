class Solution:
    def canFormArray(self,arr,pieces):
        i = 0
        while i < len(arr):
            found = False
            for piece in pieces:
                if piece[0] == arr[i]:
                    for num in piece:
                        if i >=len(arr) or arr[i]!= num:
                            return False
                        i += 1
                    found = True
                    break
            if not found:
                return False
        return True
   