def digitSum(n):
    s = 0
    while(n > 0):
        s += n % 10
        n /= 10
    return s

hh, mm = [int(x) for x in input().split()]
num = int(input())

while(True):
    num = digitSum(num)
    if(mm + 15 >= 60):
        hh += 1
        mm -= 45
    else:
        mm += 15
    if(hh > 23):
        print("ERROR")
        break
    if(num < 10):
        print('{:02}'.format(hh), '{:02}'.format(mm))
        break
