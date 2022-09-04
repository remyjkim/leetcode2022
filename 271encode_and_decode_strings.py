# Runtime: 150 ms, faster than 17.07% of Python3 online submissions for Encode and Decode Strings.
# Memory Usage: 14.5 MB, less than 21.25% of Python3 online submissions for Encode and Decode Strings.

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoder = str(len(strs))
        msg = ""
        for string in strs:
            encoder = "_".join([encoder] + [str(len(string))])
            msg = "".join([msg] + [string])
        return "_".join([encoder, msg])

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        list_len = int(s[:s.find("_")])
        s = s[s.find("_") + 1:]
        word_len = []
        for k in range(list_len):
            print(int(s[:s.find("_")]))
            word_len.append(int(s[:s.find("_")]))
            s = s[s.find("_") + 1:]
        answer = []
        for l in range(list_len):
            answer.append(s[:word_len[l]])
            s = s[word_len[l]:]
        return answer