class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashIndex = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashIndex:
                left = hashIndex[diff]
                right = i
                break
            else:
                hashIndex[nums[i]] = i
        return [left, right]


    
    def twoSum_first(self, nums: List[int], target: int) -> List[int]:
        #O(n) time complexity and O(n) space complexity, but can be done in one pass by finding the right index first
        #New attempt
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