class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<int,int>> p;
        for (int i = 0; i < position.size(); ++i) {
            p.push_back({position[i],speed[i]});
        }
        sort(p.rbegin(),p.rend());
        vector<double> st;

        for (int i = 0; i < position.size(); ++i) {
            double distance = target - p[i].first;
            st.push_back(distance / p[i].second);

            if (st.size() >= 2 && st.back() <= st[st.size() - 2]) {
                st.pop_back();
            }
        }


        return st.size();
        // 0 1 4 7
        // 1 2 2 1
        // target is 10
    }
};
