class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        pacific = [[False] * cols for _ in range(rows)]
        atlantic = [[False] * cols for _ in range(rows)]

        directions = [(1,0),(-1,0),(0,-1),(0,1)]

        psources = []
        asources = []

        for r in range(rows):
            psources.append((r, 0))
            asources.append((r, cols-1))

        for c in range(cols):
            psources.append((0, c))
            asources.append((rows-1, c))

        def bfs(source, ocean):
            q = deque(source)
            while q:
                row, col = q.popleft()
                ocean[row][col] = True
                for dx, dy in directions:
                    x = dx + row
                    y = dy + col
                    if (0 <= x < rows and 0 <= y < cols and not ocean[x][y]
                        and heights[x][y] >= heights[row][col]):
                        q.append((x, y))

        
        bfs(psources, pacific)
        bfs(asources, atlantic)
        res = []
        for r in range(rows):
            for c in range(cols):
                if pacific[r][c] and atlantic[r][c]:
                    res.append([r,c])
        return res
