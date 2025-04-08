#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#
def climbingLeaderboard(ranked, player):
    # リーダーボードのスコアの重複を削除
    ranked = sorted(set(ranked), reverse=True)
    
    res = []
    # rankedの末尾のインデックス
    i = len(ranked) - 1 

    for score in player:
        # rankedを逆順に走査、scoreよりも小さい最初の要素を見つける
        while i >= 0 and score >= ranked[i]:
            i -= 1
        # i = -1のとき　scoreはどのrankedの要素よりも大きい -> 順位は1
        # i = 0のとき　scoreは最初の要素以下 -> 順位は2
        res.append(i + 2) 
    
    return res
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
