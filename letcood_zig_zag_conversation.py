class Solution(object):      
    def convert(self, s, numRows):
        if numRows == 1 or len(s) <= numRows:
            return s
        size_middle = numRows - 2
        result = ''
        start = 0
        round_middle = 0
        index = 0
        middle = 0
        while True:
            index = start
            while index < len(s):
                result += s[index]
                index += numRows + size_middle
                
                if middle != 0:
                   ind_midl = index - middle
                   if len(s) > ind_midl:
                        result += s[ind_midl]
            if round_middle == size_middle:
                middle = 0                
            else:
                round_middle += 1
                middle = middle + 2
            if(len(s)==len(result)):
                return result
            start += 1



solution = Solution()
tt = print(solution.convert("PAYPALISHIRING", 4))

#PINALSIGYAHRPI 4
#PAHNAPLSIIGYIR 3

