class Solution {
public:
    bool check(vector<int>& nums) {
        bool is_rotated = false;
        for (std::size_t i{}; i < nums.size() - 1; ++i) {
            if (nums[i] > nums[i + 1] && !is_rotated) {
                is_rotated = true;
            } else if (nums[i] > nums[i + 1] && is_rotated) {
                return false;
            }
        }

        return (nums[nums.size()-1] > nums[0] && is_rotated) ? false : true;
    }
};


// 3 4 5 1 3 2 - false
// 3 4 5 1 2 3 1