class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        min_val = [nums[0]] * n

        for i in range(1, n):
            min_val[i] = min(min_val[i - 1], nums[i])

        stack = []

        for j in range(n - 1, -1, -1):
            if nums[j] > min_val[j]:
                while stack and stack[-1] <= min_val[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])

        return False
