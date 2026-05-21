class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = 0
        h = heights
        i, j = 0, len(h)-1
        while i < j:
            m = max(m, (j-i) * min(h[i], h[j]))
            if h[i] > h[j]:
                j -= 1
            else:
                i += 1

        return m