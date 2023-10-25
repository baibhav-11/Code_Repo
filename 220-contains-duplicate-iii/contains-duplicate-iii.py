class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0:
            return False
        
        bucket = {}
        width = valueDiff + 1
        
        for i, num in enumerate(nums):
            if i > indexDiff:
                remove_idx = nums[i - indexDiff - 1] // width
                del bucket[remove_idx]
            
            bucket_idx = num // width
            
            if bucket_idx in bucket:
                return True
            
            if bucket_idx - 1 in bucket and abs(num - bucket[bucket_idx - 1]) < width:
                return True
            
            if bucket_idx + 1 in bucket and abs(num - bucket[bucket_idx + 1]) < width:
                return True
            
            bucket[bucket_idx] = num
        
        return False

    