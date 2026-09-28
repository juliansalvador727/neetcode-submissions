class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {
        if (nums.size() == 1) return 1;
        bool increasing = (nums[0] > nums[1]) ? false : true;
        int max_subarr = 1;
        int subarr = 1;
        for (std::size_t i = 0; i < nums.size()-1; ++i) {
            int cur = nums[i];
            int next = nums[i+1];

            if (cur > next) {
                if (!increasing) {
                    subarr++;
                } else {
                    max_subarr = max(max_subarr, subarr);
                    subarr = 2;
                }
                increasing = false;
            } else if (cur < next) {
                if (increasing) {
                    subarr++;
                } else {
                    max_subarr = max(max_subarr, subarr);
                    subarr = 2;
                }
                increasing = true;
            } else {
                max_subarr = max(max_subarr, subarr);
                subarr = 1;
            }
        }

        return max(max_subarr, subarr);
    }
};