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

## 配列
対角線成分の和
```
    for i in range(n):
        l2r += arr[i][i]
        r2l += arr[i][n - 1 - i]
```

joinして出力
```
"".join(s)
" + ".join(s)
```

二次元配列
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

# 各桁の和
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