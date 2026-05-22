#include <map>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::map<int, int> count;

        for (const int& num : nums){
            count[num] += 1;
        }

        for (auto i : count) {
            if (i.second > 1) {
                return true;
            }
        }

        return false;
    }
};
