a = int(input())
if a%10 + (a//10)%10 + (a//100)%10 == (a//1000)%10 + (a//10000)%10 + (a//100000)%10 :
    print('YES')
else:
    print('NO')
