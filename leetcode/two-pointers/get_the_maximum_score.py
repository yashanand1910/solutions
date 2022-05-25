class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        x, y = 0, 0
        n1, n2 = len(nums1), len(nums2)
        total, sum1, sum2 = 0, 0, 0
        while x < n1 or y < n2:
            while y < n2 and (x == n1 or nums1[x] > nums2[y]):
                sum1 += nums2[y]
                y += 1
            while x < n1 and (y == n2 or nums1[x] < nums2[y]):
                sum2 += nums1[x]
                x += 1
            if x < n1 and y < n2 and nums1[x] == nums2[y]:
                sum1 += nums1[x]
                sum2 += nums2[y]
                total += max(sum1, sum2)
                sum1, sum2 = 0, 0
                x += 1
                y += 1
        total += max(sum1, sum2)

        return total % (10**9 + 7)

