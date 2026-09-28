class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        vector<int>arr(nums.size() + 1);
        arr[0] = 0;
        for (int i = 0; i < nums.size(); ++i) {
            arr[i+1] = nums[i] + arr[i];
        }
        for (int i = 0; i < nums.size(); ++i) {
            int right = arr[nums.size()] - arr[i + 1];
            int left = arr[i];
            if (left == right) {
                return i;
            }
        }
        return -1;
    }
};