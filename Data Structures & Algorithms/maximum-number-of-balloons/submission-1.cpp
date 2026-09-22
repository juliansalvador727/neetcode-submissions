class Solution {
public:
    int maxNumberOfBalloons(string text) {
        int b = 0; int a = 0; int l = 0; int o = 0; int n = 0;
        for (int i = 0; i < text.length(); ++i) {
            char c = text[i];
            if (c == 'b') b++;
            if (c == 'a') a++;
            if (c == 'l') l++;
            if (c == 'o') o++;
            if (c == 'n') n++;
        }
        int ans = 0;
        while (b && a && l >= 2 && o >= 2 && n) {
            b--;
            a--;
            l -= 2;
            o -= 2;
            n--;
            ans++;
        }
        return ans;

    }
};