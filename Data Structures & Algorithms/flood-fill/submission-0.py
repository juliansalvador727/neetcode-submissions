class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        cur_color = image[sr][sc]
        image[sr][sc] = color
        if cur_color == color:
            return image

        q = deque([(sr, sc)])

        visited = set()
        visited.add((sr, sc))

        while q:
            r, c = q.popleft()

            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                x, y = r + dx, c + dy

                if (0 <= x < rows and 0 <= y < cols and image[x][y] == cur_color and (x, y) not in visited):
                    image[x][y] = color
                    q.append((x, y))
        return image
        