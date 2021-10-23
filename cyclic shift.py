print("list elem cnt=")
n=int(input())
print("shift")
s=int(input())
print("input list")
A=[]
C=[]
t=0
for i in range(n):
    A.append(input())
print(A)
while t<s:
    C.append(A[len(A)-s])
    A.pop(len(A)-s)
    t+=1

print(C+A)
