class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        q = deque()

        for r in range(rows):
            if board[r][0]=="O":
                board[r][0] = "#"
                q.append((r, 0))

            if board[r][cols-1]=="O":
                board[r][cols-1] = "#"
                q.append((r, cols-1))

        for c in range(cols):
            if board[0][c]=="O":
                board[0][c] = "#"
                q.append((0, c))

            if board[rows-1][c]=="O":
                board[rows-1][c] = "#"
                q.append((rows-1, c))
        
        while q:
            row, col = q.popleft()
            for dx, dy in directions:
                x = row + dx
                y = col + dy

                if (0 <= x < rows and 0 <= y < cols and board[x][y] == "O"):
                    board[x][y] = "#"
                    q.append((x, y))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "#":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"

