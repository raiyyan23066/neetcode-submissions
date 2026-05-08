class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen:set=set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False
    