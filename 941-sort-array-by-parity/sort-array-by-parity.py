class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # Initialize two pointers, one at the beginning and one at the end of the array.
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] % 2 == 1 and nums[right] % 2 == 0:
                # Swap the elements at the left and right pointers.
                nums[left], nums[right] = nums[right], nums[left]
            
            if nums[left] % 2 == 0:
                # If the element at the left pointer is even, move the left pointer to the right.
                left += 1
            
            if nums[right] % 2 == 1:
                # If the element at the right pointer is odd, move the right pointer to the left.
                right -= 1

        return nums

        