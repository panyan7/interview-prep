from math import factorial

c = int(input())
p = int(input())
n = p * p

ans1 = c
ans2 = (c**p - c)//p
ans3 = ((c**n) - (c**p))//n
ans = ans1 + ans2 + ans3
print(ans)
