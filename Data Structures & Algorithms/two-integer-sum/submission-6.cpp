#include <map>
#include <iostream>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::map<int,int> difference;

        for (const auto& diff : difference){
            std::cout << diff.first << " " << diff.second << std::endl;
        }

        for (int i = 0; i < nums.size(); i++) {
            if (difference.count(nums[i]) != 0){
                return std::vector<int>{difference[nums[i]], i};
            }

            difference[target-nums[i]] = i;
        }
    }
};
