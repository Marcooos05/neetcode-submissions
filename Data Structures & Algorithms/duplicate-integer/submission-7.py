class Solution:
    #Review:
    #1. How interesting to think that I used to rely solely on the brute force method for such a simple question, leading to O(n^2) time complexity. Now using a hash or set to achieve O(n) time makes so much more sense. It was fun to play around to see if sets or hashmap being more memory efficient but given in this instance there were no significant savings, by right sets are supposed to be more efficient than hashmap dictionary.
    #2. Surprisingly there is value in the brute force method as well because of the space complexity of the solution being O(1), then I come to realise every method of solution has a use case where it is most ideal, it's not necessarily always about being the fastest. Then ofc there is the sorting method which uses time complexity O(nlogn) and space complexity of O(1) depending on the sorting algorithm, but it was interesting exploration.
    #3. Even on the use of set and hash at the start, there were ways to reduce the code redundancy to make it more legible and understandable, which is a considerate and polite thing to do for maintenance haha. Ultimately, the single line solution to compare the len of set and list, I do respect it, would not have come to that conclusion myself since it felt like a solution very specific to the question. Regardless, this did help with reviewing my understanding of time and space complexity and better appreciate the use of hashmaps and sets.

    #ps - saw the most memory efficient solution on Leetcode, man literally hardcoded all the True and False for every test case, like the commitment is REAL, not too sure why that itself is not the fastest solution too. Yet another apt reminder that it's not always about optimizing for the outcome, I mean as Software Engineers we should all be familiar with Overfitting... 
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

    def hasDuplicate_hashAttempt(self, nums: List[int]) -> bool:
        #using hash to possibly improve memory usage
        hashCount = {}
        for num in nums:
            if num not in hashCount:
                hashCount[num] = 1
            else:
                return True
        return False
    
    def hasDuplicate_setAttempt(self, nums: List[int]) -> bool:
        #set difference method, good runtime, memory not optimal
        #dup = set() - initally used a duplicate set to track duplicates but not actually needed, it can be simplified to return immediately on detecting a duplicate
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False