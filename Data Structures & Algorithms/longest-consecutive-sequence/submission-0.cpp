class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int result{};
        unordered_set<int> tracker(nums.begin(), nums.end());

        for (int n : nums) {
            int streak = 0;
            int cur = n;
            while (tracker.find(cur) != tracker.end()) {
                streak++;
                cur++;
            }
            result = max(result, streak);
        }
        return result;
    }
};
