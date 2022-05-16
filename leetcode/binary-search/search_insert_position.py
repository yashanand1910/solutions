class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        index = len(nums)
        
        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            else:
                index = mid
                right = mid - 1
        
        return index
        