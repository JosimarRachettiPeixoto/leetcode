class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter_already = {}
        word = ''
        result = {}
        if '' == s:
            return 0
        for index in range(len(s)):
            if not s[index] in letter_already:
                word += s[index]
                letter_already[s[index]] = index
            else:
                result[index] = len(word)
                if s[index] in word:
                    word = s[letter_already[s[index]] + 1 : index]
                    letter_already[s[index]] = index
                word += s[index]
                letter_already[s[index]] = index
        result[len(s)] = len(word)
        return  max(result.values())
            


#tmmzuxt
#dvdf
#abcb
#abcabcbb
#aabaab!bb
print(Solution().lengthOfLongestSubstring('tmmzuxt'))