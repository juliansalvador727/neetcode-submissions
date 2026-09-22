class Solution {
public:

    bool wordPattern(string pattern, string s) {
        stringstream ss(s);
        vector<string> words;
        string word;
        while (ss >> word) {
            words.push_back(word);
        }
        if (pattern.length() != words.size()) return false;
        unordered_map<char,string> mp;
        unordered_map<string,char> reverse_mp;
        for (int i = 0; i < pattern.length(); ++i) {
            char c = pattern[i];
            string w = words[i];

            if (mp.contains(c) && mp[c] != w) {
                return false;
            }

            if (reverse_mp.contains(w) && reverse_mp[w] != c) {
                return false;
            }

            mp[c] = w;
            reverse_mp[w] = c;
        }
        return true;
    }
};