class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        // Fill an array with count of all characters in magazine
        int magazineCount[26] = {0};
        
        for (string :: iterator ch = magazine.begin(); ch != magazine.end(); ch++) {
            magazineCount[int(*ch) - 97]++;
        }
        
        for(string :: iterator ch = ransomNote.begin(); ch != ransomNote.end(); ch++) {
            if (--magazineCount[int(*ch) - 97] < 0) {
                return false;
            }
        }
        
        return true;
    }
};
