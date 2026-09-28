class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        vector<int>cc(26, 0);
        for (int i = 0; i < allowed.size(); ++i) {
            cc[allowed[i] - 'a'] = true;
        }
        int ans = 0;
        for (const auto& w : words) {
            int add = 1;
            for (int i = 0; i < w.size(); ++i) {
                if (!cc[w[i] - 'a']) {
                    add = 0;
                    break;
                }
            } 
            ans += add;
        }
        return ans;
    }
};