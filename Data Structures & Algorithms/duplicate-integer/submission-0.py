class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        htable = set()
        for i in nums:
            if i not in htable:
                htable.add(i)
            else:
                return True
        return False 
        