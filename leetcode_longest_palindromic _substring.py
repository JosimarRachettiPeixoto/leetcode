class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        if len(s) == 1:
                return s
        
        word = s
        reverse = ''
        index = 0
        while True:
            if not (len(word)) >= 1:
                break
            reverse = word[index] + reverse
            if reverse not in word:
                while reverse not in word:
                    word = word[1:]
                    reverse = reverse[:-1]
                index = 0
                reverse = ''
                if index > (len(word) - 1):
                    index = 0 
                    reverse = ''
                continue  
            if reverse == word[:len(reverse)] and len(reverse) > len(result):
               result = reverse 
            if (len(word) - 1) > index:
                index += 1
        return result
    



print(Solution().longestPalindrome('abcdbbfcba'))