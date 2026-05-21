class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        prefix = [0] * N
        suff = [0] * N
        total = 0

        for i in range(1, N):
            prefix[i] = max(height[i-1], prefix[i-1])
        for i in range(N-2,-1,-1):
            suff[i] = max(height[i+1], suff[i+1])
        for i in range(1,N-1):
            product = min(prefix[i], suff[i]) - height[i]
            if product > 0:
                total += product

        print(prefix)
        print(suff)

        return total

