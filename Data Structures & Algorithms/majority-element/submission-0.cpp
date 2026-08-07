class Solution {
public:
    int majorityElement(vector<int>& nums) {
        const int majority = nums.size() / 2;
        unordered_map<int,int> mp;
        for (auto &n : nums) {
            mp[n]++;
            if (mp[n] > majority) {
                return n;
            }
        }
    }
};