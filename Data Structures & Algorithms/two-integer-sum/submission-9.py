class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Runtime 28ms | Beats 100.00%
        #Memory 7.9 MB | Beats 100.00%
        #Single pass method with O(n) time and space complexity
        #Similar complexity but more efficient in returning the immediate solution without having to prepare the hashMap beforehand
        hashIndex = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashIndex:
                return [hashIndex[diff], i]
            else:
                hashIndex[nums[i]] = i


    
    def twoSum_first(self, nums: List[int], target: int) -> List[int]:
        #O(n) time complexity and O(n) space complexity, but can be done in one pass by finding the right index first
        #two pass attempt
        hashCount = {}
        
        #O(n) time complexity to create the hashMap, O(n) space complexity
        for num in nums:
            if num in hashCount:
                hashCount[num] += 1
            else:
                hashCount[num] = 1

        for i in range(len(nums)):
            hashCount[nums[i]] -= 1
            difference = target - nums[i]

            if difference in hashCount and hashCount[difference] > 0:
                left = i
                break
        right = nums[left+1:].index(difference) + left+1

        return [left, right]