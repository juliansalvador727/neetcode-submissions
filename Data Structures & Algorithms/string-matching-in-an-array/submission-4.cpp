class Solution {
public:
    vector<string> stringMatching(vector<string>& words) {
        vector<string> ans;
        for (int i = 0; i < words.size(); ++i) {
            for (int j = 0; j < words.size(); ++j) {
                if (i == j) continue;
                string word = words[i];
                string next_word = words[j];

                if (next_word.find(word) != std::string::npos) {
                    ans.push_back(word);
                    break;
                }
            }
        }
        return ans;
    }
};