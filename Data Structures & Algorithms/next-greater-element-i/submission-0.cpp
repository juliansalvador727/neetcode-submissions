class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        for (int i = 0; i < nums1.size(); ++i) {
            int x = nums1[i];
            bool found = false;
            int ans = -1;
            for (int j = 0; j < nums2.size(); ++j) {
                int y = nums2[j];
                if (found && y > x) {
                    ans = y;
                    break;
                } else if (x == y) {
                    found = true;
                }
            }
            nums1[i] = ans;
        }
        return nums1;
    }
};