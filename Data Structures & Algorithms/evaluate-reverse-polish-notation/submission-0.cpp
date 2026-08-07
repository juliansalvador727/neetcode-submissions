class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st;

        for (auto& t : tokens) {
            if (t == "+" || t == "-" || t == "*" || t == "/") {
                int right = st.top();
                st.pop();
                int left = st.top();
                st.pop();
                if (t == "+") {
                    left += right;
                } else if (t == "-") {
                    left -= right;
                } else if (t == "*") {
                    left *= right;
                } else if (t == "/") {
                    left /= right;
                }
                st.push(left);
            } else {
                int num = stoi(t);
                st.push(num);
            }
        }
        return st.top();
    }
};
