class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #optimal memory allocation
        #Runtime 45ms|Beats 100.00%
        #Memory 9.3 MB|Beats 5.10%
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)