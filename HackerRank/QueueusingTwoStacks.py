# Enter your code here. Read input from STDIN. Print output to STDOUT

q = []
query = int(input())
for _ in range(query):
    line = input().split()
    t = int(line[0])
    if t == 1:
        n = int(line[1])
        q.append(n)
    elif t == 2:
        q.pop(0)
    else:
        print(q[0])
    # print(q)