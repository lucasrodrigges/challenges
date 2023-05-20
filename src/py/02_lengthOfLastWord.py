# leetcode
# 58. Length of Last Word

# first solution

class Solution:
    def lengthOfLastWord(self, s: str):
        result = ''
        i = len(s) - 1

        while (i >= 0):
            if s[i] == ' ':
                if not result:
                    i -= 1
                else:
                    break
            else:
                result += s[i]
                i -= 1

        return len(result)


print(
    Solution().lengthOfLastWord('Hello World'),
    Solution().lengthOfLastWord('a')
)
