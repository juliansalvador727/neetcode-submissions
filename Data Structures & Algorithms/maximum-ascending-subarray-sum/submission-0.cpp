class Solution {
public:
    int maxAscendingSum(vector<int>& nums) {
        int max_sum = 0;
        int sum = 0;
        for (int i = 0; i < nums.size() - 1; ++i) {
            int x = nums[i];
            int y = nums[i+1];
            
            sum += x;
            if (x >= y) {
                max_sum = max(sum, max_sum);
                sum = 0;
            }
        }
        // check last elem
        if (nums[nums.size()-2] < nums[nums.size()-1]) {
            sum += nums[nums.size()-1];
        }

        return max(max_sum, sum);    
    }
};