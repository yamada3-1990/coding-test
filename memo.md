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
