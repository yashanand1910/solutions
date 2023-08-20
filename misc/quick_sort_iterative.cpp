#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

using std::vector;

using list = vector<int>;

std::ostream &operator<<(std::ostream &out, const list &arr) {
  if (arr.empty())
    return out;
  out << "[ ";
  std::copy(arr.begin(), arr.end(), std::ostream_iterator<int>(out, ", "));
  out << "\b\b ]";

  return out;
}

/* Function prototypes */
void swap(int i, int j, list &arr);
void qsort(int start, int end, list &arr);

/* Constants */
const static int NELEMS = 2000;

int main() {
  // Generate large random array
  list actual_arr;
  for (int i = 0; i < NELEMS; i++) {
    actual_arr.emplace_back(rand());
  }

  // Copy the array
  list expected_arr = actual_arr;

  qsort(0, actual_arr.size() - 1, actual_arr);
  std::sort(expected_arr.begin(), expected_arr.end());

  // Check if array is sorted
  for (int i = 0; i < NELEMS; i++) {
    assert(actual_arr[i] == expected_arr[i]);
  }

  std::cout << "OK" << std::endl;

  return 0;
}

/**
 * @brief Swap two elements in an array.
 *
 * @param[in]   i   First element index
 * @param[in]   j   Second element index
 * @param[out]  arr List to swap elements in
 */
void swap(int i, int j, list &arr) {
  int temp = arr[i];
  arr[i] = arr[j];
  arr[j] = temp;
}

/** @brief Sort elements of an array.
 *
 * Uses recursive quick sort.
 *
 * @param[in]   start Starting index
 * @param[in]   end   Ending index
 * @param[out]  arr   List to sort
 */
void qsort(int start, int end, list &arr) {
  if (end - start < 1)
    return;

  // start partitioning
  int last = start;
  for (int i = start + 1; i <= end; i++) {
    if (arr[i] < arr[start]) {
      swap(i, ++last, arr);
    }
  }

  // finish partitioning
  swap(start, last, arr);

  // perform qsort on the partitions
  qsort(start, last - 1, arr);
  qsort(last + 1, end, arr);
}

/** @brief Sort elements of an array.
 *
 * Uses iterative quick sort.
 *
 * @param[in]   start Starting index
 * @param[in]   end   Ending index
 * @param[out]  arr   List to sort
 */
void qsort_i(int start, int end, list &arr) {
  if (end - start < 1)
    return;

  // start partitioning
  int last = start;
  for (int i = start + 1; i <= end; i++) {
    if (arr[i] < arr[start]) {
      swap(i, ++last, arr);
    }
  }

  // finish partitioning
  swap(start, last, arr);

  // perform qsort on the partitions
  qsort(start, last - 1, arr);
  qsort(last + 1, end, arr);
}
