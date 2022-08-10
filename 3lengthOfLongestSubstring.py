class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur_max = 0
        start, end = 0, 0
        for i in s:
            if i not in s[start:end]:
                end += 1
                if end - start > cur_max:
                    cur_max = end - start
            else:
                start_from = s[start:end].index(i)
                start += (start_from + 1)
                end += 1

            print(f"looked at {i} and s[start:end] is {s[start:end]}")

        return cur_max


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur_max = 0
        track = ""
        for i in s:
            if i not in track:
                track += i
                cur_max = max(len(track), cur_max)
            else:
                track = track[track.index(i)+1:]+i
        return cur_max