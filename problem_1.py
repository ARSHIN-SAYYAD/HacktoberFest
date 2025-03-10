def threeSum(self, nums):
    res = []
    nums.sort()
    for i in range(len(nums)-2):
        if i > 0 and (nums[i] == nums[i-1]):
            continue
        l=0, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l +=1 
            elif s > 0:
                r -= 1
            else:
                res.append(s)
                while l < r and (nums[l] == nums[l+1]):
                    l += 1
		while l < r and nums[r] == nums[r-1]:
            r -= 1
            l += 1; r -= 1
                
    return res
