class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #Trying to consider a more computationally efficient way to solve the problem 
        #Reversal order seems like the key to this question
        arr = arr[::-1]
        highest = -1
        for i in range(len(arr)):
            n = arr[i]
            arr[i] = highest
            if n > highest:
                highest = n
        return arr[::-1]

    def replaceElements_first(self, arr: List[int]) -> List[int]:
        #Goal is to replace the current index with the max of index+1
        #simplest solution will be to brute for loop then max of the remaining subarray
        #O(n^2) time complexity and O(1) space complexity since it is mutable, not bad
        #Runtime 39ms|Beats 24.70%
        #Memory 7.7 MB|Beats 99.56%
        for i in range(len(arr)):
            if i == len(arr)-1:
                arr[i] = -1
            else:
                arr[i] = max(arr[i+1:])
        
        return arr