class Solution {
public:
  vector<int> platesBetweenCandles(string s, vector<vector<int>> &queries) {
    vector<int> res, candles;

    // store candles indices
    for (size_t i = 0; i < s.length(); ++i) {
      if (s[i] == '|') candles.push_back(i);
    }
    
    for (const auto& query : queries) {
      const int lefti = query[0], righti = query[1];
      int start, end;
      int plates = 0;

      // find leftmost candle after lefti
      start = 0, end = candles.size() - 1;
      int leftc = -1;
      while (start <= end) {
        int mid = start + ((end - start) / 2);
        if (candles[mid] >= lefti) {
          leftc = mid;
          end = mid - 1;
        } else {
          start = mid + 1;
        }
      }

      // find rightmost candle before righti
      start = 0, end = candles.size() - 1;
      int rightc = -1;
      while (start <= end) {
        int mid = start + ((end - start) / 2);
        if (candles[mid] <= righti) {
          rightc = mid;
          start = mid + 1;
        } else {
          end = mid - 1;
        }
      }

      // count plates between the candles
      if (leftc != -1 && candles[leftc] < righti) {
        plates = candles[rightc] - candles[leftc] - (rightc - leftc);
      }

      res.push_back(plates);
    }

    return res;
  }
};
