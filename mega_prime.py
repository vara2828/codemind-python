n=int(input())
c=0
r=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
        if c>2:
            break
if c==2:
    r+=1
n=str(n)
for i in n:
    d=0
    for j in range(1,int(i)+1):
        if int(i)%j==0:
            d+=1
            if d>2:
                break
    if d==2:
        r+=1
if r==len(n)+1:
    print("Mega Prime")
else:
    print("Not Mega Prime")
