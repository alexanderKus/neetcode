class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        l , r = 1, k

        while l < r:
            nk = l + ((r - l)//2)
            th = 0
            for x in piles:
                th += math.ceil(x/nk)
            #print(f'l: {l}, r: {r}, k: {k}, nk: {nk}, th: {th}, h: {h}')
            if th <= h:
                k = min(k, nk)
                r = nk
            else:
                l = nk + 1
        
        return k