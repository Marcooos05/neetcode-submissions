class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Review
        #1. As usual comparing anagrams can always use a hash or list to count the characters instead of sorting the string to compare. But it really depends on the space availability, using a hashmap would be O(n) space and O(n) time but sorting would use O(nlogn) time but O(1) space since we reuse the space
        #2. Well I learnt that we cannot use list as the key for dictionaries in python, coool(?) then we cannot .join a list of integers, only applicable for a list of strings. Then again in one of the test cases, the count was "10","1", "0" and it would be the same as "1", "0", "10" if you joined them so it was better to use a tuple as the key instead.

        hashGroup = {}
        for word in strs:
            counter = [0] *26
            for char in word:
                #love this way of getting the index lol
                counter[ord(char) - ord('a')] += 1
            
            #converting the list to a tuple to be used as a key for a hash
            tupleCount = tuple(counter)
            if tupleCount in hashGroup:
                hashGroup[tupleCount].append(word)
            else:
                hashGroup[tupleCount] = [word]

        return list(hashGroup.values())