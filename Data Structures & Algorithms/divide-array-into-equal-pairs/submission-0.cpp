class Solution {
public:
    bool divideArray(vector<int>& nums) {
        unordered_map<int,int> mp;
        for (const auto& n : nums) {
            mp[n] += 1;
        }
        for (const auto& n : mp) {
            if (n.second % 2 == 1) return false;
        }
        return true;
    }
};