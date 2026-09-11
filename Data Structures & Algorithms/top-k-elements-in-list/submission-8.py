class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Review
        #1. Refresher on Bucket sort. Interesting to use a known list of buckets to basically fit numbers into an already sorted list then append them to attain O(n) time complexity. If the range of values is known, we can actl iterate through the list once, to count the frequency and reconstruct the list which is technically O(n + k) time where k is the possible unique values.
        
        hashCount = {}
        freq = [[] for i in range(len(nums)+1)]
        for i in nums:
            hashCount[i] = 1 + hashCount.get(i, 0)
        for n, c in hashCount.items():
            freq[c].append(n)

        output = []
        for values in freq[::-1]:
            for val in values:
                output.append(val)
                if len(output) == k:
                    return output