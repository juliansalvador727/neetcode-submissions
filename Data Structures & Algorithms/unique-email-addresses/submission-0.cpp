class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        std::unordered_map<string,int> mp;
        for (const auto& email : emails) {
            bool is_domain = false;
            string valid_email = "";
            for (int i = 0; i < email.length(); ++i) {
                if (email[i] == '@') {
                    is_domain = true;
                } else if (!is_domain && email[i] == '.') {
                    continue;
                } else if (!is_domain && email[i] == '+') {
                    int j = i;
                    while (j < email.length() && email[j] != '@') {
                        j++;
                    }
                    i = j;
                    is_domain = true;
                }
                valid_email += email[i];
            }
            mp[valid_email] += 1;
        }
        return mp.size();
    }
};

// + and . applies to local name