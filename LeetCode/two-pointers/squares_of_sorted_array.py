class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        list = [0]*len(nums)
        left, right = 0, len(nums)-1
        i = len(nums)-1
        while i >= 0:
            if nums[right] >= abs(nums[left]):
                list[i] = nums[right]**2
                i -= 1
                right -= 1
            else:
                list[i] = nums[left]**2
                i -= 1
                left += 1
        return list
        