class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        if (!checkRows(board)) return false;
        if (!checkColumns(board)) return false;

        for (int row = 0; row < 9; row += 3) {
            for (int col = 0; col < 9; col += 3) {
                if(!checkBoxes(board, row, col)) return false;
            }
        }

        return true;
    }

    bool checkRows(vector<vector<char>>& board) {
        for (std::size_t i = 0; i < 9; ++i) {
            std::unordered_set<char> tracker;
            for (std::size_t j = 0; j < 9; ++j) {
                char val = board[i][j];
                if (val == '.') continue;

                if (tracker.contains(val)) return false;

                tracker.insert(val);
            }
        }
        return true;
    }
    bool checkColumns(vector<vector<char>>& board) {
        for (std::size_t i = 0; i < 9; ++i) {
            std::unordered_set<char> tracker;
            for (std::size_t j = 0; j < 9;++j) {
                char val = board[j][i];
                if (val == '.') continue;
                if (tracker.contains(val)) return false;
                tracker.insert(val);
            }
        }
        return true;
    }

    bool checkBoxes(vector<vector<char>>& board, int x, int y) {
        unordered_set<char> tracker;
        for (std::size_t i = x; i < x + 3; ++i) {
            for (std::size_t j = y; j < y + 3; ++j) {
                char val = board[i][j];
                if (val == '.') continue;
                if (tracker.contains(val)) return false;
                tracker.insert(val);
            }
        }

        return true;
    }

};

