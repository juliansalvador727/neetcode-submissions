class Solution {
public:
    vector<int> findMissingAndRepeatedValues(vector<vector<int>>& grid) {
        unordered_map<int, int> mp;
        int n = grid.size();
        for (int i = 1; i <= n * n; ++i) {
            mp[i] = 0;
        }
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                mp[grid[i][j]]++;
            }
        }
        int a = 0;
        int b = 0;
        for (const auto& [key, value] : mp) {
            if (value == 2) {
                a = key;
            } else if (value == 0) {
                b = key;
            }
        }
        return {a, b};
    }
};