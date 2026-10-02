class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        vector<int>fb;
        fb.push_back(0);
        for (const auto& f : flowerbed) {
            fb.push_back(f);
        }
        fb.push_back(0);

        for (int i = 1; i < fb.size()-1; ++i) {
            if (!fb[i] && !fb[i-1] && !fb[i+1]) {
                fb[i] = 1;
                n--;
            }
        }

        return (n <= 0) ? 1 : 0;
    }
};