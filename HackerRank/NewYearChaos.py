#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # print(q)
    l = len(q)
    cnt = 0
    for i in range(l):  
        # print("diff: ", q[i] - i - 1) 
        if q[i] - i - 1 > 2:
            print("Too chaotic")
            return
        
        # 最大2回だけ実行
        # 最大2人を抜かしているので、調べるべきは現在の位置 i より前の最大2つの位置にいる人たち
        # もし人 q[i] が最大2人を抜かして現在の位置 i にいるなら、その人が抜かした可能性のある人の今の位置は、q[i] + 1 または q[i] + 2
        # q= [2 1 5 3 4]の場合、i=2(q[i]=5の人)の位置にいるとき、5の人は、5-1=4の人と、5-2=3の人を抜かした可能性がある(元の配列が[1 2 3 4 5]だから)

        # q[i]が示すのは、iの位置にいる人の元の位置
        # もしこの人が前に移動したとすると、その移動によって元の位置が q[i] - 1 や q[i] - 2 の人たちが後ろに押しやられた可能性
        # 12345だったら、5が3か4の人を抜かした可能性がある

        # i より前のインデックス j にいる人 q[j]を調べる
        # 現在見ている人 (q[i]) より前にいて、かつ元の位置がその人よりも後ろだった人
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                cnt += 1
    print(cnt)
            

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
