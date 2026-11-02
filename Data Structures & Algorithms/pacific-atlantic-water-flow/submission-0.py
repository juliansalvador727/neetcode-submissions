class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        pacific = [[False] * cols for _ in range(rows)]
        atlantic = [[False] * cols for _ in range(rows)]

        psources = []
        asources = []

        for c in range(cols):
            psources.append((0, c))
            asources.append((rows-1, c))
        
        for r in range(rows):
            psources.append((r, 0))
            asources.append((r, cols-1))

        def bfs(source, ocean):
            q = deque(source)
            while q:
                r, c = q.popleft()
                ocean[r][c] = True
                for dx, dy in directions:
                    x = r + dx
                    y = c + dy
                    if (0 <= x < rows and 0 <= y < cols and not ocean[x][y] and heights[x][y] >= heights[r][c]):
                        q.append((x,y))

        bfs(psources, pacific)
        bfs(asources, atlantic)

        res = []
        for r in range(rows):
            for c in range(cols):
                if pacific[r][c] and atlantic[r][c]:
                    res.append([r, c])

        return res