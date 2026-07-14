class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result;
        std::unordered_map<string, int> mp;

        for (std::size_t i = 0; i < strs.size(); ++i ) {
            string hash = "";
            vector<int> freq(26, 0);
            for (char ch : strs[i]) freq[ch - 'a'] += 1;

            for (int i = 0; i < 26; ++i )
            {
                hash += to_string(freq[i]);
                hash += "$";
            }

            if (mp.count(hash) == 0) {
                mp[hash] = result.size();
                result.push_back({});
            }

            result[mp[hash]].push_back(strs[i]);
        }

        return result;
    }
};
