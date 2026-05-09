class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        target=0
        curr_sum=0
        res=[]
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            target=-nums[i]
            if i > 0 and nums[i]==nums[i-1]:
                continue
            while left < right :
                curr_sum=nums[left]+nums[right]
                if curr_sum > target:
                    right-=1
                elif curr_sum<target :
                    left+=1
                elif curr_sum==target:
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left < right and nums[left]==nums[left-1]:
                        left+=1
                    while left < right and nums[right ]== nums[right+1]:
                        right-=1
        return res