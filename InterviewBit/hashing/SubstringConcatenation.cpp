vector<int> Solution::findSubstring(string A, const vector<string> &B) {
    unordered_map<string, int> words;
    int wordLength = B[0].size();
    vector<int> output;
    
    if (A.size() < B.size() * wordLength) return output;
    
    for (auto word : B) {
        if (words.find(word) == words.end()) words.insert({word, 1});
        else words[word]++;
    }
    
    int i = 0;
    while (i < A.size() - wordLength + 1) {
        int length = 0;
        unordered_map<string, int> buffer;
        
        while (words.find(A.substr(i, wordLength)) != words.end()) {
            if (buffer.find(A.substr(i, wordLength)) == buffer.end()) buffer.insert({A.substr(i, wordLength), 1});
            else {
                if (buffer[A.substr(i, wordLength)] < words[A.substr(i, wordLength)]) buffer[A.substr(i, wordLength)]++;
                else break;
            }
            length++;
            i += wordLength;
        }
        
        if (length == B.size()) output.push_back(i - B.size() * wordLength);
        i = i - wordLength * length + 1;
    }
    
    return output;
}
