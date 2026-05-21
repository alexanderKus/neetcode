class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        longest, l, unique = 1, 0, set()
        unique.add(s[0])
        for r in range(1, len(s)):
            if s[r] in unique:
                while s[r] in unique and l < r:
                    print(f'2. s[{l}]: {s[l]},s[{r}]: {s[r]},  u: {unique}')
                    unique.remove(s[l])
                    l += 1
                    print(f'3. s[{l}]: {s[l]}, s[{r}]: {s[r]}, u: {unique}')
            unique.add(s[r])
            print(f'1. s[{l}]: {s[l]}, s[{r}]: {s[r]}, u: {unique}')
            longest = max(longest, len(unique))
        return longest
                
                

