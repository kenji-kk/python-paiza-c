n = int(input())
ans = 0
for i in range(n):
    com = int(input())
    if ans < com:
        ans  = com
print(ans)
