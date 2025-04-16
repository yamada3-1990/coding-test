## 解き方
グリッド系の問題は、周期(パターン)を見つけ、周期ごとの状態を求める

2sum問題
-> 与えられた数値の配列（またはリスト）の中から、特定の合計値になる2つの数値の組み合わせを見つけ出す問題
愚直にforループは時間的に厳しい
ハッシュ値を用いる
```
def icecreamParlor(m, arr):
    # 空のハッシュマップ seen を作成
    seen = {}
    for i, price in enumerate(arr):
        # 目標金額 m との差額 complement = m - price を計算
        complement = m - price
        if complement in seen:
        # 差額を埋めれるキーがある = 現在の金額と足してmにできる
            return seen[complement] + 1, i + 1
        # なかったら追加
        seen[price] = i
    # 解が見つからない場合は None を返す（問題の制約によっては不要）
    return None 
```

## dict
各要素のキーと値に対してforループ処理
```
for k, v in d.items():
    print(k, v)
```

各要素のキーに対してforループ処理
```
for k in d.keys():
    print(k)
```

各要素の値に対してforループ処理
```
for v in d.values():
    print(v)
```

## format
小数点以下の有効桁数を指定する

```
f = 0.123456789012345
print(f)  # 0.123456789012345

# 有効桁数10桁
result = format(f, '.10f')  
result = '{:.10f}'.format(f)  
result = '{0:.10f}'.format(f)  
result = f'{f:.10f}'  
result = format(f, '.10e')  

print(result)  # 0.1234567890

```

## n進数
```
# 10to2
bin(5) # '0b101'

# 2to10
0b101 # 5

# nto16
hex(0b10010) # '0x12'
```
| 論理積 (AND) | 論理和 (OR) | 排他的論理和 (XOR) | 反転 (NOT) |
|---|---|---|---|
| \& | \| | ^ | ~ |

### 0のビット数
nを2進数の文字列に変換→'0' の数をカウント→"0b(語頭のやつ)"の分のカウントを引く
```
bin(n).count('0') - 1
# nに対してn+i == n^iを満たす整数 i の数
2 ** z 
```
n + i == n ^ i(XOR)
↓
n と i のビットごとのAND演算の結果が 0
↓
n & i == 0(XOR)



## 配列
対角線成分の和
```
    for i in range(n):
        l2r += arr[i][i]
        r2l += arr[i][n - 1 - i]
```

同時にインデックスも取得
```
l = ['Alice', 'Bob', 'Charlie']
for i, name in enumerate(l):
    print(i, name)
# 0 Alice
# 1 Bob
# 2 Charlie
```

joinして出力
```
"".join(s)
" + ".join(s)
```

###二次元配列
```
# n個の空リストを持つ二次元配列
# [[], [], [], ...]
arr = [[] for _ in range(n)]

# 2*3の配列
a = [[0 for j in range(3)] for i in range(2)]

# numpy
import numpy as np
arr = np.zeros((2, 3))

# 列の数を取得
cols = len(matrix[0]) 

# 列を取得
column = [row[1] for row in matrix]
```

ある(x, y)の周りの処理
```
# 8近傍(上下左右角)
dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

# 4近傍(上下左右)
dx = [0, 0, 1, -1] 
dy = [1, -1, 0, 0] 


for y in range(H):
  for x in range(W):
    for a, b in zip(dx, dy):
      i, j = x + a, y + b
      if 0 <= i < W and 0 <= j < H:
        # 配列[i][j]を使った処理
```

ソート
昇順
```
sorted(A)
sort(A) # A自体がソートされる
```

降順
```
sorted(A, reverse=True)
sort(A, reverse=True) # A自体がソートされる
```

## 文字列

全て小文字/大文字に変換
```
s = s.lower()
s = s.Upper()
```
置き換え
```
s = s.replace(" ", "")
```

文字列をシフトする(暗号とかのやつ)
```
# ord() 関数で文字のASCIIコードを取得
k %= 26 (シフトする文字数)
if char.islower():
    shifted_char = chr(((ord(char) - ord('a') + k) % 26) + ord('a'))
```

## 各桁の和
```
n = "12345"
result = sum(map(int, n)) # 15
```

## Tower Breakersについて
* 塔の数(m)が偶数の場合：
    * プレイヤー1が塔を減らすと、プレイヤー2は同じ塔を減らすことで、ゲームの状態をプレイヤー1のターン前の状態に戻すことができます。
    * つまり、プレイヤー2は常にプレイヤー1の動きを真似できるため、プレイヤー1は最終的に動けなくなり、プレイヤー2が勝ちます。
* 塔の数(m)が奇数の場合：
    * プレイヤー1が最初の動きで塔を減らすと、プレイヤー2はプレイヤー1の動きを真似ることができません。
    * プレイヤー1は常に有利な状態を維持できるため、最終的にプレイヤー2が動けなくなり、プレイヤー1が勝ちます。

## 階乗
```
# 2のべき乗かを判断
if n & (n-1) == 0:
```

```
# n以下の最大の2の累乗
while p * 2 <= n:
    p *= 2
```

## リストノード
単方向リスト(linked list)を逆順にする
1 -> 2 -> 3 -> NULLの場合、while文中では、
```
res = None(NULL)
-- 1回目
curr = 1
llist = 2
curr.next = None (curr = 1 -> None)
res = 1
-- 2回目
curr = 2
llist = 3
curr.next = 1 (curr = 2 -> 1 -> None)
res = 2
-- 3回目
curr = 3
llist = None
curr.next = 3 (curr = 3 -> 2 -> 1 -> None)
res = 3
```
```
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next

def reverse(llist):
    res = None
    while llist:
        curr = llist 
        llist = llist.next
        # 前に追加していく
        curr.next = res 
        res = curr
    return res
```  
双方向リスト(linked list)を逆順にする
```
def reverse(llist):
    # currはllistと同じノードを参照しているだけ
    curr = llist
    prev = None
    
    while curr:
        # 一時的に次のノードを保持
        next_node = curr.next
        
        # currの次のノードをひとつ前のノードに変更
        curr.next = prev
        # currの前のノードを次のノードに変更
        curr.prev = next_node
        

        prev = curr
        # currを更新
        curr = next_node
    return prev
```