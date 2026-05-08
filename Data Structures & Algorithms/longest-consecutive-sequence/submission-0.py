class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        curr_num=1
        longest=0
        for i in num_set:
            if i-1 not in num_set:
                curr_num=i
                curr_streak=1
                while curr_num + 1 in num_set:
                    curr_num+=1
                    curr_streak+=1
                longest=max(longest,curr_streak)
        return longest 