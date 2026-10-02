class Solution {
public:
    bool isPathCrossing(string path) {
        set<pair<int,int>> pos;
        int x = 0; int y = 0;
        pos.insert({x, y});

        for (const auto& ch : path) {
            if (ch == 'N') y++;
            else if (ch == 'S') y--;
            else if (ch == 'E') x++;
            else if (ch == 'W') x--;

            if (pos.count({x,y})) return true;
            pos.insert({x,y});
        }
        return false;
    }
};