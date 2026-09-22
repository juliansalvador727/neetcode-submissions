class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
        int ans = 0;
        unordered_map<char,int> mp_ch;
        for (const auto& ch : chars) mp_ch[ch] += 1;
        for (const auto& w : words) {
            int length = w.length();
            bool good = true;
            unordered_map<char,int> mp;
            for (const auto& ch : w) mp[ch] += 1;
            for (const auto& ch : w) {
                if (mp[ch] > mp_ch[ch]) { 
                    good = false;
                    break;
                }
            }
            if (good) {
                ans += length;
                good = false;
            }
        }
        return ans;
    }
};