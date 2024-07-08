class Solution:
    def reverse(self, x: int) -> int:
        neg = -1 if x < 0 else 1
        x_string = str(abs(x))
        x_reverse = x_string[::-1]
        result = int(x_reverse)
        if result.bit_length() > 31:
            return 0
        return result * neg



print(Solution().reverse(-123))