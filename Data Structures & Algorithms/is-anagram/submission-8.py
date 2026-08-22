class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #worth to try a hash or an array method. Given the constraints of the alphabets even those will be space complexity of O(1) so worth a shot
        #in this case i would prefer using an array over a hash given that arrays generally use less space than hash
        #Runtime 51ms|Beats 100.00%
        #Memory 8.5 MB|Beats 41.02%
        #O(n+m) time complexity
        count = [0] * 26
        for char in s:
            count[ord(char)- ord('a')]  += 1
        for char in t:
            count[ord(char)- ord('a')]  -= 1

        return count == [0]*26

    def isAnagram_first(self, s: str, t: str) -> bool:
        #optimal memory allocation
        #Runtime 45ms|Beats 100.00%
        #Memory 9.3 MB|Beats 5.10%

        #O(nlogn + mlogm) time complexity
        return sorted(s) == sorted(t)