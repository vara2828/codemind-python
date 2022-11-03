n=int(input())
c=[]
while n>0:
    r=n%10
    n=n//10
    c.append(r)
print(max(c))
    