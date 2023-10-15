class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_max, second_max, third_max = float('-inf'), float('-inf'), float('-inf')
        distinct_max_set = set()

        for num in nums:
            if num in distinct_max_set:
                continue
            
            if num > first_max:
                first_max, second_max, third_max = num, first_max, second_max
            elif num > second_max:
                second_max, third_max = num, second_max
            elif num > third_max:
                third_max = num

            distinct_max_set.add(num)

        if len(distinct_max_set) < 3:
            return first_max
        else:
            return third_max
