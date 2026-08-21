class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashCount = {}
        for num in nums:
            if num in hashCount:
                hashCount[num] += 1
            else:
                hashCount[num] = 1
        for val in hashCount.values():
            if val > 1:
                return True
        return False