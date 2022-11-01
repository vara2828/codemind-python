n,m=map(int,input().split())
k=abs(m-n)
if k==1 or k==9:
    print('Yes')
else:
    print('No')