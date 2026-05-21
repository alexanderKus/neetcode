class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        longest, l, unique = 1, 0, set()
        unique.add(s[0])
        for r in range(1, len(s)):
            if s[r] in unique:
                while s[r] in unique and l < r:
                    unique.remove(s[l])
                    l += 1
            unique.add(s[r])
            longest = max(longest, len(unique))
        return longest
                
                

