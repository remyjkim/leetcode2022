#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countPalindromes' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def countPalindromes(s):
    # Write your code here
    n = len(s)
    # start with zero
    res = 0
    if n <= 0:
        return 0

    # create a dp problem
    dp = [[None for c in s] for c in s]

    # True for all one-letters
    for i in range(n):
        dp[i][i] = 1
        res += 1

    # two letters
    for j in range(n - 1):
        dp[j][j + 1] = int(s[j] == s[j + 1])
        res += int(dp[j][j + 1])
    print("before the 3 and onward:", res)
    # dynamic for 3 and onwards
    for l in range(3, n + 1):
        i = 0
        for k in range(i + l - 1, n):
            print(i, "th: ", s[i], "/ ", k, "th: ", s[k], "/dp[i+1][k-1]:", dp[i + 1][k - 1], "/res: ", res)
            if dp[i + 1][k - 1] and (s[i] == s[k]):
                dp[i][k] = 1
            else:
                dp[i][k] = 0

            res += int(dp[i][k])
            i += 1
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = countPalindromes(s)

    fptr.write(str(result) + '\n')

    fptr.close()
