class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left = 0;
        int right = heights.size() - 1;
        int water = 0;
        int ans = 0;
        while (left < right) {
            int height_one = heights[left];
            int height_two = heights[right];
            
            int water = (right - left) * min(height_one,height_two);
            ans = max(ans, water);
            if (height_one > height_two) {
                right--;
            } else  {
                left++;
            }
        }

        return ans;
    }
};
