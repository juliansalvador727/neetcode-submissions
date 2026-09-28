class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        if (!numRows) return {};
        if (numRows == 1) return {{1}};
        vector<vector<int>>pt;
        pt.push_back({1});
        for (int i = 1; i < numRows; ++i) {
            vector<int>prev_row;
            prev_row.push_back(0);
            for (const auto& x : pt[i - 1]) {
                prev_row.push_back(x);
            }
            prev_row.push_back(0);
            vector<int>row;
            for (int j = 0; j < prev_row.size() - 1; ++j) {
                row.push_back(prev_row[j] + prev_row[j + 1]);
            }
            pt.push_back(row);
        }
        return pt;
    }

};


// 0 1 0
// 0 1 1 0
