class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashCount = {}
        for num in nums:
            if num not in hashCount:
                hashCount[num] = 1
            else:
                return True
                
        return False