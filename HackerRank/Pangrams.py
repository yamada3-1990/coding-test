#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    dic = {}
    s = s.lower()
    s = s.replace(" ", "")
    print(s)
    
    for i in s:
        # print(i)
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
            
    if len(dic) != 26:
        return "not pangram"
    else:
        return "pangram"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
