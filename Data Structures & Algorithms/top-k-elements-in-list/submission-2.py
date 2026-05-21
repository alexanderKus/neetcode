class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        
        sort = dict(reversed(sorted(d.items(), key=lambda item: item[1])))

        res = list()
        for key,_ in sort.items():
            res.append(key)
            if len(res) >= k:
                break
        
        return res
