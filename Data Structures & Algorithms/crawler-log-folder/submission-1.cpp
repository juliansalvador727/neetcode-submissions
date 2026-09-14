class Solution {
public:
    int minOperations(vector<string>& logs) {
        stack<string> st;
        for (const auto& log : logs) {
            if (log != "./" && log != "../") {
                st.push(log);
            } else if (log == "../" && st.size() != 0) {
                st.pop();
            } else {
                continue;
            }
        }
        return st.size();
    }
};