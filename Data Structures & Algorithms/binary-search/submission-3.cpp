class Solution {
public:
    int search(vector<int>& nums, int target) {
        auto it = std::ranges::lower_bound(nums, target); 
        return it != nums.end() && *it == target 
        ? static_cast<int>(it - nums.begin()) : -1;
    }
};
