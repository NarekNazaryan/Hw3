def prime(n):
     if n==2:
         return True
     for i in range(2,int(n**0.5)+1):
         if n%i==0:
             return False
     return True
n=int(input())
if n%2==0:
    for i in range(2,n):
         if prime(i)==True:
          for j in range(i,n):
             if i+j==n and prime(j)==True:
                 k=i
                 t=j
                 break
    print(n,"=",k,"+",t)
else:
    print("odd")




