class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefixsum = [0] * N
        sufixsum = [0] * N
        prefixsum[0] = sufixsum[N-1] = 1
        for i in range(1,N):
            prefixsum[i] = nums[i-1] * prefixsum[i-1]
        for i in range(N-2, -1, -1):
            sufixsum[i] = nums[i+1] * sufixsum[i+1]

        result = [prefixsum[i] * sufixsum[i] for i in range(N)]
        return result