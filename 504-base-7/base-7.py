class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        is_negative = num < 0
        num = abs(num)
        result = []

        while num > 0:
            remainder = num % 7
            result.append(str(remainder))
            num //= 7

        if is_negative:
            result.append("-")

        return "".join(result[::-1])
