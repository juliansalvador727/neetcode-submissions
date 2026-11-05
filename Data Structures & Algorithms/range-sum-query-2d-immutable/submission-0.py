class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        rows, cols = len(matrix), len(matrix[0])
        prefix = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                prefix[r][c] = matrix[r][c]
                if r > 0:
                    prefix[r][c] += prefix[r - 1][c]
                if c > 0:
                    prefix[r][c] += prefix[r][c - 1]
                if r > 0 and c > 0:
                    prefix[r][c] -= prefix[r - 1][c - 1]
        self.prefix = prefix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        prefix = self.prefix
        total = prefix[row2][col2]

        if row1 > 0:
            total -= prefix[row1 - 1][col2]
        if col1 > 0:
            total -= prefix[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            total += prefix[row1 - 1][col1 - 1]

        return total


# Your NumMatrix object will be instantiated and called as such: *
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)