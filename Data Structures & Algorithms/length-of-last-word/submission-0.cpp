class Solution {
public:
    int lengthOfLastWord(string s) {
        int length = 0;
        bool is_last_word = false;
        for (int i = s.length() - 1; i >= 0; --i) {
            if (s[i] == ' ' && is_last_word) {
                return length;
            } else if (s[i] != ' '){
                is_last_word = true;
                length++;
            }
        }
        return length;
    }
};