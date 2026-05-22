#include <unordered_map>

class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> charCount;

        for (char& c : s){
            charCount[c] += 1;
        }

        for (char& c : t){
            charCount[c] -= 1;

            if (charCount[c] < 0) {
                return false;
            }
        }

        for (auto& count : charCount) {
            if (count.second != 0) {
                return false;
            }
        }

        return true;
    }
};
