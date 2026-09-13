class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int max_ones = 0;
        int cur_ones = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] == 1) {
                cur_ones++;
            } else {
                max_ones = max(max_ones, cur_ones);
                cur_ones = 0;
            }
        }
        return max(max_ones, cur_ones);
    }
};

// wait why am i being retarded rn what am i missing
// edge case 1 1 1 1 1 1... never updates 