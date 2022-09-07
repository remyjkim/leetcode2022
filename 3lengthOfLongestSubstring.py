# Runtime: 52 ms, faster than 98.91% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Runtime은 개 랜덤인듯
# Memory Usage: 14.1 MB, less than 49.61% of Python3 online submissions for Longest Substring Without Repeating Characters.
# TODO: learning - Be careful with sliding window, and think carefully about where to start over

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        cur_str = ""
        for i in range(len(s)):
            if s[i] not in cur_str:
                cur_str += s[i]
                max_length = max(max_length, len(cur_str))
            else:
                ind = cur_str.index(s[i])
                cur_str = cur_str[ind + 1:] + s[i]
            # print(i,"th: ", cur_str)
        return max_length
