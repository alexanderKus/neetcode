class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        pq = []
        res = []
        l = 0

        for i in range(k):
            heapq.heappush(pq, (-nums[i], i))

        res.append(-pq[0][0])
        l += 1

        for r in range(k, N):
            #print(pq)
            m, i = -pq[0][0], pq[0][1]

            while i < l:
                heapq.heappop(pq)
                if len(pq) == 0: break
                m, i = -pq[0][0], pq[0][1]

            heapq.heappush(pq, (-nums[r], r))
            res.append(-pq[0][0])
            l += 1

        return res