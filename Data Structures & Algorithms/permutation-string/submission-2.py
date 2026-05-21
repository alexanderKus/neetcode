class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        l = 0
        lookup = defaultdict(int)
        count = defaultdict(int)

        for i in range(len(s1)):
            lookup[s1[i]] += 1

        r = 0
        while r < len(s2):
            while r - l < len(s1):
                count[s2[r]] += 1
                r += 1
            print(lookup)
            print(count)
            is_p = True
            for k,v in lookup.items():
                print(k,v)
                if k not in count or count[k] != v:
                    is_p = False
                    break
            
            if is_p:
                return True
            
            count[s2[l]] -= 1
            l += 1

        return False
            