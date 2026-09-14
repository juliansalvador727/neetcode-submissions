class Solution {
public:
    bool digits_are_same(int n) {
        int ones = n % 10;
        int tens = (n % 100) / 10;
        int hundreds = n / 100;

        if (ones == tens && tens == hundreds) return true;
        return false;
    }
    string largestGoodInteger(string num) {
        char one, two, three;
        int max_ans_found = 0;
        string big = "";
        string ans = "";
        for (int i = 0; i < num.length()-2; ++i) {
            ans = num.substr(i,3);
            if (!digits_are_same(stoi(ans))) {
                continue;
            } else {
                if (big == "") { big = ans; }
                else {
                    big = to_string(max(stoi(big), stoi(ans)));
                }
            }
        }
        if (big == "0") return "000";
        return big;
    }
};