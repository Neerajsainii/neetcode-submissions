class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums) -1
        for i in range(0,len(nums)):
            mid  = first + (last-first)//2
            if nums[mid] > target:
                last = mid - 1
            elif nums[mid] < target:
                first = mid + 1
            else:
                return mid
        return -1