class Solution {
public:
    int maxScore(string s) {
        string left = "";
        string right = "";
        int score = 0;
        for (int i = 0; i < s.length() - 1; ++i) {
            left = s.substr(0,i+1);
            right = s.substr(i+1, s.length()-1);

            int current_score = 0;
            for (int j = 0; j < left.length(); ++j) { if (left[j] == '0') current_score++; } 
            for (int j = 0; j < right.length(); ++j) { if (right[j] == '1') current_score++; }
            score = max(score, current_score);
        }
        return score;
    }
};