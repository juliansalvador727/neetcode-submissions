class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size() - 1;
        while (l <= r) {
            int m = l + (r - l) / 2;
            int mid = nums[m];
            if (mid == target) {
                return m;
            } else if (mid > target) {
                r = m - 1;
            } else if (mid < target) {
                l = m + 1;
            }
        }
        return -1;
    }
};
