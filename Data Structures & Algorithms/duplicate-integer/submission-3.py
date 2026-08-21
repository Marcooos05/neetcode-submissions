class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #set difference method, good runtime, memory not optimal
        dup = set()
        seen = set()
        for num in nums:
            if num in seen:
                dup.add(num)
            else:
                seen.add(num)
        print(seen, dup)
        return len(dup) != 0