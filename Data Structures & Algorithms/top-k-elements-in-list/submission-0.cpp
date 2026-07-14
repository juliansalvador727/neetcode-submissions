class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int> frequency; // store [number, count]

        for (const auto& num : nums) {
            frequency[num] += 1;
        }
        std::vector<std::pair<int,int>> entries;

        for (const auto&[number, count] : frequency) {
            entries.push_back({count, number});
        }

        std::sort(entries.begin(), entries.end(), greater<>());

        vector<int> r;
        for (int i = 0; i < k; ++i)
        {
            r.push_back(entries[i].second);
        }

        return r;
    }
};
