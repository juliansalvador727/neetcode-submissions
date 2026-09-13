class Solution {
public:
    bool isSubsequence(string s, string t) {
        // 2 ptr
        int i{}, j{};
        while (i < s.length() && j < t.length()) {
            if (s[i] == t[j]) {
                i++;
            }
            j++;
        }
        return i == s.length();
    }
};