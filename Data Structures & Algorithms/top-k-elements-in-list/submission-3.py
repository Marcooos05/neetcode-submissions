class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashCount = {}
        for i in nums:
            if i in hashCount:
                hashCount[i] += 1
            else:
                hashCount[i] = 1
        
        enumeratedData = list(hashCount.items())

        sortedData = sorted(enumeratedData, key=lambda x: x[1], reverse = True)
        
        output = []
        for i in range(k):
            output.append(sortedData[i][0])
        
        return output