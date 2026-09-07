class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashGroup = {}
        for word in strs:
            counter = [0] *26
            for char in word:
                counter[ord(char) - ord('a')] += 1
            
            # for i in range(len(counter)):
            #     counter[i] = str(counter[i])

            tupleCount = tuple(counter)
            if tupleCount in hashGroup:
                hashGroup[tupleCount].append(word)
            else:
                hashGroup[tupleCount] = [word]

        return list(hashGroup.values())