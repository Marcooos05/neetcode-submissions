class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        for i in range(len(nums)):
            unique = set(nums[i+1:])
            if (target - nums[i]) in unique:
                left = i
                break
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