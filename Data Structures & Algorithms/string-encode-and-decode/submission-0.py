class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f'#{len(s)}#{s}' for s in strs)

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        start = 1
        while start < len(s):
            end = start + 1
            while s[end] != '#':
                end += 1
            l = int(s[start:end])
            print(f's: {start}, e:{end}, l:{l}, x: {s[end+1:end+1+l]}')
            res.append(s[end+1:end+1+l])
            start = end + l + 2
        return res