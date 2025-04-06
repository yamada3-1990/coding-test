#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    dic = {}
    for i in s:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    # 各文字の出現回数一覧(回数のみ)
    freq = list(dic.values())
    # 出現回数の重複なしバージョン(出現回数の種類)
    unique_freq = list(set(dic.values()))
    print(freq)
    print(unique_freq)
    
    # 出現回数が1種類=すべての文字が同じ回数出現
    if len(unique_freq) == 1:
        return "YES"
        
    # 出現回数が2種類
    if len(unique_freq) == 2:
        # 出現回数の1種類目
        f1 = unique_freq[0]
        # 出現回数の2種類目
        f2 = unique_freq[1]
        
        # f1回出現した文字が1つのみかつ、それが1回のみ出現
        if (freq.count(f1) == 1 and f1 == 1) or (freq.count(f2) == 1 and f2 == 1):
            return "YES"
        # f1とf2の回数の差が1かつ、f1回出現した文字が1つ
        elif abs(f1 - f2) == 1 and (freq.count(f1) == 1 or freq.count(f2) == 1):
            return "YES"
     
    return "NO"
        
        
    

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
