class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                rotated = nums[i:] + nums[:i]
                return rotated == sorted(nums)
        
        return True

