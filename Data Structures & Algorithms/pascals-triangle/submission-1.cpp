class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        if (!numRows) return {};
        if (numRows == 1) return {{1}};
        vector<vector<int>>pt;
        for (int i = 0; i < numRows; ++i) {
            vector<int> row(i+1, 1);
            for (int j = 1; j < i; ++j) {
                row[j] = pt[i - 1][j - 1] + pt[i - 1][j];
            }
            pt.push_back(row);
        }
        return pt;
    }

};


// 0 1 0
// 0 1 1 0
