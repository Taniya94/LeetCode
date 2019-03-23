class Solution():
    def missingPositiveInteger(self,nums):
        if 1 not in nums:
            return 1
        nums.sort()
        # print len(nums)
        for i in range(0,len(nums)):
            if nums[i]>0:
                c=nums[i]+1
                if c not in nums:
                    return c


s=Solution()
print s.missingPositiveInteger([2,-1,-2,1,4])
