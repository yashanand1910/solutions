vector<int> Solution::twoSum(const vector<int> &A, int B) {
    unordered_map<int, int> list; vector<int> pair;
    for (int i = 0; i < A.size(); i++) {
            unordered_map<int, int>::iterator it = list.find(A[i]);
            if (it != list.end()) {
                pair.push_back(it->second);
                pair.push_back(i + 1);
                return pair;
            }
        list.insert({{B - A[i], i + 1}});
    }
    return pair;
}
