def prime(a):
    for j in range(2,a//2+1):
        if a%j==0:
            return True
    else:
        return False

n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        if prime(i):
            c+=1
print(c+1)