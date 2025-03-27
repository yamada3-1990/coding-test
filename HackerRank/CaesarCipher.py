#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


# k %= 26  # kが26以上の場合の処理

#     result = []
#     for char in s:
#         if char.islower():
#             shifted_char = chr(((ord(char) - ord('a') + k) % 26) + ord('a'))
#         elif char.isupper():
#             shifted_char = chr(((ord(char) - ord('A') + k) % 26) + ord('A'))
#         else:
#             shifted_char = char
#         result.append(shifted_char)

#     return "".join(result)


def caesarCipher(s, k):
    l_alpha = "abcdefghijklmnopqrstuvwxyz"
    u_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    k %= 26
    l = l_alpha[k:] + l_alpha[:k]
    u = u_alpha[k:] + u_alpha[:k]

    dicl = {}
    dicu = {}
    for i in range(26):
        dicl[l_alpha[i]] = l[i] 
        dicu[u_alpha[i]] = u[i] 
    res = ""
    for i in s:
        if i.islower():
            res += dicl[i]
        elif i.isupper():
            res += dicu[i]
        else:
            res += i
            
    print(dicl)
    return res
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
