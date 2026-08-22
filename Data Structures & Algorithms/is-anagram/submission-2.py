class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #optimal memory allocation
        return sorted(s) == sorted(t)