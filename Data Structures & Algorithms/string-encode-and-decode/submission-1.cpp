class Solution {
public:

    string encode(vector<string>& strs) {
        string result = "";
        for (size_t i = 0; i < strs.size(); ++i) {
            result += to_string(strs[i].length()) + "$" + strs[i];
        }
        return result;
    }

    vector<string> decode(string s) {
        vector<string> result;
        std::size_t i = 0;
        while (i < s.size()) {
            std::size_t delimiter = i;
            while (delimiter < s.size() && s[delimiter] != static_cast<char>(36)) {
                    delimiter++;
            }
            int length = stoi(s.substr(i, delimiter - i));

            result.push_back(s.substr(delimiter + 1, length));

            i = delimiter + 1 + length;
        }

        return result;
    }
};
