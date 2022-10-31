n=int(input())
s=0
for f in range(1,n):
    if n%f==0:
        s+=f
    
if n==s:
    print("True")
else:
    print("False")
