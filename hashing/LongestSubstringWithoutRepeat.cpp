int Solution::lengthOfLongestSubstring(string A) {
    unordered_map<char, int> charMap;
    int maxLength = INT_MIN, i = 0;
    
    while (i < A.size()) {
        if (charMap.find(A[i]) != charMap.end()) {
            int length = charMap.size();
            maxLength = max(maxLength, length);
            i = charMap[A[i]];
            charMap.clear();
        } else {
            charMap.insert({A[i], i});
        }
        i++;
    }
    
    int length = charMap.size();
    maxLength = max(maxLength, length);
    
    return maxLength;
}
