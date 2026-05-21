class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        res = []

        l, r = 0, k

        while r <= N:
            m = max(nums[l:r])
            res.append(m)
            r += 1
            l += 1

        return res