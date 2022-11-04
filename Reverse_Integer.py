n=int(input())
s=''
if n<0:
    n=str(abs(n))
    s+="-"
else:
    n=str(n)
s+=n[::-1]
n=int(s)
print(n)