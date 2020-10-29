q = int(input())
while(q > 0):
    a, b, t = map(int, input().split())
    ans = (t // 2) * (a - b)
    if(t % 2 != 0):
        ans += a
    print(ans)
    q -= 1
