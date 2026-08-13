class Solution {
public:
    int trap(vector<int>& height) {
        if (height.size() == 0) return 0;
        int n = height.size();

        int l = 0;
        int r = n - 1;
        int left_max = height[l];
        int right_max = height[r];
        int ans = 0;
        while (l < r) {
            if (left_max < right_max) {
                l++;
                left_max = max(left_max, height[l]);
                ans += left_max - height[l];
            } else {
                r--;
                right_max = max(right_max, height[r]);
                ans += right_max - height[r];
            }
        }
        return ans;
    }
};
