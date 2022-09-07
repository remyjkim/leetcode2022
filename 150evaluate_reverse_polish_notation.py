# Used the solution
# Runtime: 84 ms, faster than 76.84% of Python3 online submissions for Evaluate Reverse Polish Notation.
# Memory Usage: 14.4 MB, less than 25.75% of Python3 online submissions for Evaluate Reverse Polish Notation.
# TODO: learning - stack can be appended in the middle. utilize that! RPN always uses two top elements!
#  When number, just add to stack, when operation, go on do the work and append again

class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(l+r)
                elif t == "-":
                    stack.append(l-r)
                elif t == "*":
                    stack.append(l*r)
                else:
                    stack.append(int(float(l)/r))
        return stack.pop()
