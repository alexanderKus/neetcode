class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""

        l = 0
        lookup = defaultdict(int)
        count = defaultdict(int)
        candidates = []

        for i in range(len(t)):
            lookup[t[i]] += 1

        def match(x=None) -> bool:
            for k,v in lookup.items():
                if k not in count or count[k] < v:
                    return False

            return True

        print(lookup)
        r = 0
        while r < len(s):
            while not match() and r < len(s):
                #print(f'l: {l}, r: {r}')
                count[s[r]] += 1
                r += 1

            print(count)
            had_match = False
            while match():
                had_match = True
                #print(f'l: {l}, r: {r}')
                count[s[l]] -= 1
                l += 1
                
            if had_match:
                candidates.append(s[l-1:r])

        print(candidates)
        return "" if len(candidates) == 0 else min(candidates, key=len)




