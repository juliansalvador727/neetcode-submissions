class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int num_rows = matrix.size();
        int num_cols = matrix[0].size();

        int top = 0;
        int bot = num_rows - 1;
        // int row = bot + (top - bot) / 2;
        while (top <= bot) {
            int row = bot + (top - bot) / 2;
            if (target > matrix[row][num_cols-1]) {
                top = row + 1;
            } else if (target < matrix[row][0]) {
                bot = row - 1;
            } else {
                break;
            }
        }
        if (!(top <= bot)) return false;

        int row = bot + (top - bot) / 2;
        int l = 0;
        int r = num_cols - 1;
        while (l <= r) {
            int m = l + (r - l) / 2;
            if (target > matrix[row][m]) {
                l = m + 1;
            } else if (target < matrix[row][m]) {
                r = m - 1;
            } else {
                return true;
            }
        }
        return false;
    }
};
