class Solution {
public:
    int maxDifference(string s) {
        unordered_map<char, int> mp;
        for (const auto& ch : s) {
            mp[ch] += 1;
        }
        int min_even {1<<30};
        int max_odd{};
        for (auto [key, value] : mp) {
            if (value % 2 == 0) {
                min_even = min(min_even, value);
            } else if (value % 2 == 1){
                max_odd = max(max_odd, value);
            }
        }
        return max_odd - min_even;
    }
};