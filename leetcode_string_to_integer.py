class Solution:
    def myAtoi(self, s: str) -> int:
        s, num, negative = s.strip(), '', False
        for idx in range(len(s)):
            if (s[idx] == '-' or s[idx] == '+') and idx == 0:
                if s[idx] == '-':
                     negative = True
                continue
            if s[idx].isnumeric():
                num = num + s[idx]
                continue
            if not s[idx].isnumeric():
                break           
        if len(num) == 0:
            return 0
        if int(num).bit_length() > 31:
            return -2147483648 if negative else 2147483647
        return int(num) * -1 if negative else int(num)


print(Solution().myAtoi("0-1"))