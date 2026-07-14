class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> tracker;
        for (std::size_t i{0}; i < nums.size(); ++i) {
            if (tracker.contains(nums[i])) return true;

            tracker.insert(nums[i]);
        }
        return false;
    }
};