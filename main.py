n=int(input())
summ1 = 0
summ2 = 0
number = n
digit = n % 10
t = 0
while n > 0:
        digit1 = n % 10
        n = n // 10
        summ1 = summ1 + digit1
        t += 1
t=4
while t/2>0:
    digit2=number%10
    number=n//10
    summ2=summ2+digit2
    t-=1
print(summ1,summ2)

