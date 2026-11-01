class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        n = rows * cols

        parent = list(range(n))
        size = [1] * n

        def find(cell):
            while cell != parent[cell]:
                parent[cell] = parent[parent[cell]]
                cell = parent[cell]
            return cell

        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b: # if we are already connected dont double count
                return size[root_a]
            
            # attach smaller to larger
            if size[root_a] < size[root_b]: 
                root_a, root_b = root_b, root_a
            
            parent[root_b] = root_a
            size[root_a] += size[root_b]

            return size[root_a]
        max_area = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue
                cell = r * cols + c
                max_area = max(max_area, 1)
                # only check down and right

                for dx, dy in [(0,1), (1,0)]:
                    x = r + dx
                    y = c + dy

                    if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
                        neighbor = x * cols + y
                        merged_size = union(cell, neighbor)
                        max_area = max(max_area, merged_size)

        return max_area