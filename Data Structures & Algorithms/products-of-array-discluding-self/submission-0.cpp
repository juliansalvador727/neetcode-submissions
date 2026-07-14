class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> prefix_list(nums.size(), 1);
        vector<int> suffix_list(nums.size(), 1);
        
        vector<int> result(nums.size());

        for (std::size_t i = 1; i < nums.size(); ++i) {
            prefix_list[i] = prefix_list[i - 1] * nums[i - 1];
        }

        for (int i = nums.size() - 2; i >= 0; --i) {
            suffix_list[i] = suffix_list[i+1] * nums[i + 1];
        }

        for (std::size_t i = 0; i < nums.size(); ++i) {
            result[i] = suffix_list[i] * prefix_list[i];
        }

        return result;
    }
};
