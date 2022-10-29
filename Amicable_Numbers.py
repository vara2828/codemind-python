a=int(input())
b=int(input())

s=0
s1=0
for f in range(1,a+1):
    if a%f==0 and a!=f:
        s+=f
for i in range(1,b+1):
    if b%i==0 and b!=i:
        s1+=i
if s==b and s1==a:
    print("Amicable")
else:
    print('Not Amicable')