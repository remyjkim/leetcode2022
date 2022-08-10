# Runtime: 313 ms, faster than 66.87% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 21.7 MB, less than 32.18% of Python3 online submissions for Product of Array Except Self.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [1]* length
        for i, n in enumerate(nums[:-1]):
            answer[i+1] = answer[i]*n
        R = 1
        for j, m in enumerate(reversed(nums)):
            # print(f'{answer} / {j} / {m}')
            answer[length-1-j] *= R
            R *= m
        return answer

# Runtime: 466 ms, faster than 16.04% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 21.4 MB, less than 44.65% of Python3 online submissions for Product of Array Except Self.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [1] * length
        L, R = 1, 1
        for i in range(length):
            answer[i] *= L
            L *= nums[i]
        for j in reversed(range(length)):
            # print(f'{answer} / {j} / {m}')
            answer[j] *= R
            R *= nums[j]
        return answer

