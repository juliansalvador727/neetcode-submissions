class Solution {
public:
    int calPoints(vector<string>& operations) {
        stack<int> st;
        int running = 0;
        for (auto o : operations) {
            if (o == "+") {
                int last = st.top();
                st.pop();
                int prev = st.top();
                int sum = last + prev;

                st.push(last);
                st.push(last + prev);
                running += sum;
            }
            else if (o == "C") {
                running -= st.top();
                st.pop();
            }
            else if (o == "D") {
                st.push(st.top() * 2);
                running += st.top();
            } else {
                st.push(stoi(o));
                running += st.top();
            }
        }
        return running;
    }
};