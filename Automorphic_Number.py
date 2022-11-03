n=int(input())
l=len(str(n))
a=n*n
m=a%pow(10,l)
if m==n:
    print("Automorphic Number")
else:
    print('Not an Automorphic Number')