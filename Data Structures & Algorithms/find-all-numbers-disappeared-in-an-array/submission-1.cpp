class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        int n = nums.size();

        vector<bool>arr(n, false);
        vector<int>ans;
        for (const auto& m : nums) {
            arr[m - 1] = true;
        }
        for (int i = 1; i <= n; ++i) {
            if (!arr[i - 1]) {
                ans.push_back(i);
            }
        }
        return ans;

    }
};