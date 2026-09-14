class Solution {
public:
    int maxScore(string s) {
        int score = 0;
        int right_ones = 0;
        int left_zeroes = 0;
        
        for (char c : s) {
            if (c == '1') {
                right_ones += 1;
            }
        }

        for (int i = 0; i < s.length() - 1; ++i) {
            if (s[i] == '0') {
                left_zeroes++; 
            } else {
                right_ones--;
            }
            score = max(score, left_zeroes + right_ones);
        }
        return score;
    }
};