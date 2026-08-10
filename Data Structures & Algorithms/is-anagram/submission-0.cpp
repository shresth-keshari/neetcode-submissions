class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false; // Important check

        std::vector<int> hashlist(26, 0);
        for (int i = 0; i < s.length(); i++) {
            hashlist[s[i] - 'a']++;
            hashlist[t[i] - 'a']--;
        }

        // Correct usage of std::all_of
        return all_of(hashlist.begin(), hashlist.end(), [](int i) {return i == 0;});
    }
};