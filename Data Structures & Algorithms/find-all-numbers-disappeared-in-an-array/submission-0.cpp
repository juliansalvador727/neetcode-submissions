class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans;
        unordered_map<int,int> mp;
        for (int i = 1; i <= n; ++i) {
            mp[i] = 0;
        }
        for (int i = 0; i < n; ++i) {
            mp[nums[i]] += 1;
        }
        for (const auto& [key, value] : mp) {
            if (value == 0) {
                ans.push_back(key);
            }
        }
        return ans;

    }
};