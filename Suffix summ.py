n=int(input())
A=[]
B=[]
for i in range(n):
    A.append(float(input()))
for j in range(n):
    summ=0
    for k in range(j,n):
        summ=summ+A[k]
    B.append(summ)
print(A,B)
        