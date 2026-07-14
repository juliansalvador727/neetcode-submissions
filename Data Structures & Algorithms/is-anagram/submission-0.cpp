class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char,int> s_map;
        std::unordered_map<char,int> t_map;

        for (std::size_t i{}; i < s.length(); ++i)
        {
            s_map[s[i]] += 1;
        }

        for (std::size_t j{}; j < t.length(); ++j)
        {
            t_map[t[j]] += 1; 
        }

        return s_map == t_map;
    }
};
