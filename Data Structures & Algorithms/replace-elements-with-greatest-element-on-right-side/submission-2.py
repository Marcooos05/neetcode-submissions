class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #Trying to consider a more computationally efficient way to solve the problem 
        #Reversal order seems like the key to this question
        #By doing this it is one iteration of O(n) time complexity
        #Runtime 27ms|Beats 94.10%
        #Memory 7.9 MB|Beats 20.99%
        n = len(arr)
        ans = [0] * n
        rightMax = -1
        for i in range(n - 1, -1, -1):
            ans[i] = rightMax
            rightMax = max(arr[i], rightMax)
        return ans

        

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