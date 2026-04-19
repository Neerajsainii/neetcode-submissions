class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i,n in enumerate(nums):
            s[n] = i
        for i,n in enumerate(nums):
            diff = target - n
            if diff in s and s[diff] != i:
                return [i,s[diff]]
        return []