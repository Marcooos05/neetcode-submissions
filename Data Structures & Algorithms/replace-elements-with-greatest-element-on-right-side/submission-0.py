class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        pass
        #Goal is to replace the current index with the max of index+1
        #simplest solution will be to brute for loop then max of the remaining subarray

        for i in range(len(arr)):
            if i == len(arr)-1:
                arr[i] = -1
            else:
                arr[i] = max(arr[i+1:])
        
        return arr