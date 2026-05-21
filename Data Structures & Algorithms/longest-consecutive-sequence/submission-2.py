class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        setnums = set(nums)
        minvalue, maxvalue = nums[0], nums[0]
        for num in nums:
            minvalue = min(minvalue, num)
            maxvalue = max(maxvalue, num)

        longest = 1
        current = 1
        for value in range(minvalue+1, maxvalue+1):
            if value in setnums:
                current += 1
                longest = max(longest, current)
            else:
                current = 0

        return longest

