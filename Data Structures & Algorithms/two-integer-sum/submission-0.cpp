class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> nums_map;
        for (std::size_t i = 0; i < nums.size(); ++i ) {
            int complement = target - nums[static_cast<int>(i)];
            if (nums_map.contains(complement)) {
                return { nums_map[complement], static_cast<int>(i) };
            }
            nums_map[nums[i]] = static_cast<int>(i);
        }
    }
};
