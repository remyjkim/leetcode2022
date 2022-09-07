# Runtime: 30 ms, faster than 95.90% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 13.9 MB, less than 26.45% of Python3 online submissions for Valid Parentheses.
class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        paren = {"}": "{", ")": "(", "]": "["}
        for i in s:
            # TODO: learning - if opening, can open freely, but when closing, the answers are predetermined
            if i in paren.values():
                a.append(i)
            elif i in paren:
                if len(a) == 0 or a.pop() != paren[i]:
                    return False
        if a == []:
            return True
        else:
            return False


# Runtime: 57 ms, faster than 29.19% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 13.9 MB, less than 26.45% of Python3 online submissions for Valid Parentheses.


class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        for i in s:
            if i in "{([":
                a.append(i)
            elif i in "})]":
                if len(a)==0:
                    return False
                if a[-1] == "{" and i =="}":
                    a.pop()
                elif a[-1] == "[" and i =="]":
                    a.pop()
                elif a[-1] == "(" and i ==")":
                    a.pop()
                else:
                    return False
        if len(a)==0:
            return True