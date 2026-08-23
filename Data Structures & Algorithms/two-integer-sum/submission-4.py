class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Kind of just brute force in terms of attempting, not sure what is the thot process will review again tmr, for now I believe the time complexity is O(n^2) and space is O(n) cos the creation of the set is O(n) complexity both in time and space so will need to relook at it to achieve O(n) time complexity.
        #For now ill just end the day with a successful attempt, not optimize but it did the job I guess
        left = 0
        #O(n^2) cos set creation is O(n) time complexity dang...
        for i in range(len(nums)):
            unique = set(nums[i+1:])
            if (target - nums[i]) in unique:
                left = i
                break
        #index is O(n) time complexity
        right = nums[left+1:].index(target - nums[left]) + left+1
        return [left, right]


    def failed(self, nums: List[int], target: int) -> List[int]:
        #Got trashed in a versus which was a similar question to this, so ill use a two pointer method
        #what a fool, i assumed it was a sorted list
        left = 0
        right = len(nums) - 1
        while (nums[left] + nums[right]) != target:
            if (nums[left] + nums[right]) > target:
                right -= 1
            elif (nums[left] + nums[right]) < target:
                left += 1
        return [left, right]