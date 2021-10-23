def polidrom(n):
    summ=0
    number=n
    if n<10:
        return True
    while n>0:
        digit=n%10
        n=n//10
        summ=summ*10+digit
    if summ==number:
        return True
    else:
        return False
a=int(input())
b=int(input())
A=[]
for i in range(a,b+1):
    if polidrom(i)==True:
        A.append(i)
print(A)