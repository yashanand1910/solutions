class Solution {
public:
  bool canEatBananas(vector<int> &piles, int k, int h) {
    long hours = 0;
    for (const auto &pile : piles) {
      hours += ceil((double)pile / k);
    }
    return hours <= h;
  }

  int minEatingSpeed(vector<int> &piles, int h) {
    int start = 1, end = pow(10, 9);
    int res = end;
    while (start <= end) {
      int k = start + ((end - start) / 2);
      if (canEatBananas(piles, k, h)) {
        res = k;
        end = k - 1;
      } else {
        start = k + 1;
      }
    }
    return res;
  }

  // HELPERS
  int max_element(vector<int> &arr) {
    int max = 0;
    for (const auto& element : arr) {
      if (element > max) max = element;
    }
    return max;
  }
};
