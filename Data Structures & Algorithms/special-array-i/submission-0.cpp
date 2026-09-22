class Solution {
public:
    bool isArraySpecial(vector<int>& nums) {
        if (nums.size() == 1) return true;
        for (int i = 0; i < nums.size() - 1; ++i) {
            int num_one = nums[i];
            int num_two = nums[i+1];

            if (num_one % 2 == 0 && num_two % 2 == 1) {
                continue;
            } else if (num_one % 2 == 1 && num_two % 2 == 0) {
                continue;
            } else {
                return false;
            }
        }
        return true;
    }
};