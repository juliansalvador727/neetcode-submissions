class Solution {
public:
    int calPoints(vector<string>& operations) {
        stack<int> st;
        for (auto o : operations) {
            if (o == "+") {
                int last = st.top();
                st.pop();

                int prev = st.top();

                st.push(last);
                st.push(last + prev);
            }
            else if (o == "C") {
                st.pop();

            }
            else if (o == "D") {
                st.push(st.top() * 2);
            } else {
                st.push(stoi(o));
            }
        }
        int total = 0;
        while (!st.empty()) {
            total += st.top();
            st.pop();
        }
        return total;
    }
};