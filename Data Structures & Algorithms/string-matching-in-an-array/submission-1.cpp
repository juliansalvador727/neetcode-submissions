class Solution {
public:
    vector<string> stringMatching(vector<string>& words) {
        unordered_set<string> st;
        for (int i = 0; i < words.size(); ++i) {
            for (int j = 0; j < words.size(); ++j) {
                if (i == j) continue;
                string word = words[i];
                string next_word = words[j];

                if (word.find(next_word) != std::string::npos) {
                    st.insert(next_word);
                }
            }
        }
        vector<string> ans;
        for (auto const& s : st) {
            ans.push_back(s);
        }

        return ans;
    }
};