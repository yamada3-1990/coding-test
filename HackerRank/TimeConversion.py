#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

### AM/PMから24時間表記への変換は、基本的に「時 (hour)」の部分のみを考慮すればよい

def timeConversion(s):
    hour = int(s[:2])
    minute = s[3:5]
    second = s[6:8]
    am_pm = s[8:10]

    if am_pm == "PM" and hour != 12:
        hour += 12
    elif am_pm == "AM" and hour == 12:
        hour = 0

    return "{:02d}:{}:{}".format(hour, minute, second)

def timeConversion(s):
    hour = int(s[0:2])
    minute = int(s[3:5])
    second = int(s[6:8])
    ch = s[8:10]
    total = hour*60*60 + minute*60 + second
    if ch == "AM" and total >= 12*60*60:
        total -= 12*60*60
    if ch == "PM" and total <= 12*60*60:
        total += 12*60*60
    hh = total // 3600
    mm = (total - hh*3600) // 60
    ss = total - hh*3600 - mm*60
    shh = str(hh)
    smm = str(mm)
    sss = str(ss)
    if len(shh) < 2:
        shh = "0" + shh
    if len(smm) < 2:
        smm = "0" + smm
    if len(sss) < 2:
        sss = "0" + sss
    
    print(shh + ":" + smm + ":" + sss)
    return shh + ":" + smm + ":" + sss

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
