class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashCount = {}
        freq = [[] for i in range(len(nums)+1)]
        for i in nums:
            hashCount[i] = 1 + hashCount.get(i, 0)
        for n, c in hashCount.items():
            freq[c].append(n)

        output = []
        for values in freq[::-1]:
            output += values
        
        return output[:k]