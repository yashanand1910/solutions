class Trie {
    public:
        unordered_map<char, Trie> next;
        int word_index = -1;

        void insert(string s, int i, int word_index) {
            if (i == s.length()) {
                this->word_index = word_index;
                return;
            }
            if (!this->next.count(s[i])) this->next[s[i]] = Trie();
            this->next[s[i]].insert(s, i+1, word_index);
        }
};

class Solution {
public:
    vector<pair<int, int>> get_directions(vector<string>& matrix, int i, int j) {
        vector<pair<int, int>> dirs {make_pair(i+1, j), make_pair(i, j+1), make_pair(i-1, j), make_pair(i, j-1)};
        vector<pair<int, int>> possible_dirs;
        for (pair<int, int> dir: dirs) {
            if (0 <= dir.first && dir.first < matrix.size() && 0 <= dir.second && dir.second < matrix[0].size()) {
                possible_dirs.push_back(dir);
            }
        }
        return possible_dirs;
    }

    void dfs(int i, int j, Trie* cur, string word, vector<string>& matrix, vector<bool>& found) {
        if (cur->word_index > -1) {
            found[cur->word_index] = true;
            cur->word_index = -1;
        }
        for(pair<int, int> dir: get_directions(matrix, i, j)) {
            if (matrix[dir.first][dir.second] != '&' && cur->next.count(matrix[dir.first][dir.second])) {
                char prev = matrix[dir.first][dir.second];
                matrix[dir.first][dir.second] = '&';
                dfs(dir.first, dir.second, &(cur->next[prev]), word + prev, matrix, found);
                matrix[dir.first][dir.second] = prev;
            }
        }
    }

    vector<string> findWords(vector<vector<char>>& matrix, vector<string>& words) {
        // add words to trie
        Trie trie = Trie();
        for (int i=0; i < words.size(); i++) {
            trie.insert(words[i], 0, i);
        }

        vector<bool> found(words.size(), false);
        Trie cur = trie;
        for (int i = 0; i < matrix.size(); i++) {
            for (int j = 0; j < matrix[0].size(); j++) {
                if (trie.next.count(matrix[i][j])) {
                    string s = "";
                    char prev = matrix[i][j];
                    matrix[i][j] = '&';
                    dfs(i, j, &(trie.next[prev]), s + prev, matrix, found);
                    matrix[i][j] = prev;
                }
            }
        }

        vector<string> res;
        for (int i=0; i < found.size(); i++) {
            if (found[i]) {
                res.push_back(words[i]);
            }
        }

        return res;
    }
};
