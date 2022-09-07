# Used Solution
# TODO: learning - We just need the max length! Just move the pointers along, and think carefully on when we need to change the start pointer to move the sliding window
#  Also, as long as we just keep the max lenght as a variable, we won't miss out on the max case using the sliding window

# Runtime: 119 ms, faster than 95.33% of Python3 online submissions for Longest Repeating Character Replacement.
# Memory Usage: 14 MB, less than 19.07% of Python3 online submissions for Longest Repeating Character Replacement.

def characterReplacement(self, s, k):
    maxf = res = 0
    count = collections.Counter()
    for i in range(len(s)):
        count[s[i]] += 1
        maxf = max(maxf, count[s[i]])
        if res - maxf < k: # more room for switching
            res += 1
        else: # no room, need to move the start pointing onward
            count[s[i - res]] -= 1
    return res


def characterReplacement(self, s, k):
    maxf = i = 0
    count = collections.Counter()
    for j in range(len(s)):
        count[s[j]] += 1
        maxf = max(maxf, count[s[j]])
        if j - i + 1 > maxf + k: # no more room for switching, need to move the start pointer
            count[s[i]] -= 1
            i += 1
    return len(s) - i

#Java version
# public int characterReplacement(String s, int k) {
#     int len = s.length();
#     int[] count = new int[26];
#     int start = 0, maxCount = 0, maxLength = 0;
#     for (int end = 0; end < len; end++) {
#         maxCount = Math.max(maxCount, ++count[s.charAt(end) - 'A']);
#         while (end - start + 1 - maxCount > k) {
#             count[s.charAt(start) - 'A']--;
#             start++;
#         }
#         maxLength = Math.max(maxLength, end - start + 1);
#     }
#     return maxLength;
# }