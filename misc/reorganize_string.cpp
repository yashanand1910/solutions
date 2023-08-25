#include <iostream> // cin
#include <stack>
#include <string>        // getline, string
#include <unordered_map> // unordered_map

void print_map(std::unordered_map<char, int> &map) {
  for (auto &[ch, count] : map) {
    std::cout << ch << ": " << count << std::endl;
  }
}

bool dfs(std::stack<char> &res, std::unordered_map<char, int> &counts,
         int len) {
  if (res.size() == len) {
    return true;
  }

  for (auto &[ch, count] : counts) {
    if (!res.empty() && (ch == res.top() || count == 0)) {
      continue;
    }
    count--;
    res.push(ch);
    if (dfs(res, counts, len))
      return true;
    res.pop();
    count++;
  }

  return false;
}

std::string reorganize_string(std::string s) {
  std::unordered_map<char, int> counts;
  for (char c : s) {
    counts[c]++;
  }

  std::stack<char> st;

  dfs(st, counts, s.length());

  std::string res = "";
  while (!st.empty()) {
    res += st.top();
    st.pop();
  }
  return res;
}

int main() {
  std::string s;
  std::getline(std::cin, s);
  std::string res = reorganize_string(s);
  if (res.size() == 0) {
    std::cout << "Impossible" << std::endl;
    return 0;
  }
  std::unordered_map<char, int> s_counter;
  std::unordered_map<char, int> res_counter;
  for (char c : s) {
    if (s_counter.count(c)) {
      s_counter[c] += 1;
    } else {
      s_counter[c] = 1;
    }
  }
  for (char c : res) {
    if (res_counter.count(c)) {
      res_counter[c] += 1;
    } else {
      res_counter[c] = 1;
    }
  }
  if (s_counter != res_counter) {
    std::cout << "Not rearrangement" << std::endl;
    return 0;
  }
  for (int i = 0; i < res.size() - 1; i++) {
    if (res[i] == res[i + 1]) {
      std::cout << "Same character at index " << i << " and " << i + 1 << '\n';
    }
  }
  std::cout << "Valid" << std::endl;
}
