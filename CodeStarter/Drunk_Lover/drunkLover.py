q = int(input())
while(q > 0):
    a, b, t = map(int, input().split())
    if(t % 2 == 0):
        ans = (t // 2) * (a - b)
    else:
        ans = (t // 2) * (a - b)
        ans += a
    print(ans)
    q -= 1
