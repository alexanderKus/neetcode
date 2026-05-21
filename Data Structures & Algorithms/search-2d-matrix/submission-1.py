class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])

        def to1d(x,y): return x * N + y
        def to2d(x): return x // N, x % N
        
        l, r = 0, M * N - 1
        mid = (M * N) //2

        while l <= r:
            print(l, mid, r)
            x, y = to2d(mid)
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                l = mid + 1
            else:
                r = mid - 1

            mid = l + (r-l)//2

        return False