class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char,char> mp;
        unordered_map<char,char> mp_r;
        for (int i = 0; i < s.length(); ++i) {
            if (mp.contains(s[i]) && mp[s[i]] != t[i] ||
                mp_r.contains(t[i]) && mp_r[t[i]] != s[i])
             {
                return false;
            }
            mp[s[i]] = t[i];
            mp_r[t[i]] = s[i];
        }
        return true;
    }
};