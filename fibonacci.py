n=int(input())
l=[0,1,1]
for i in range(3,n):
    l.append(l[i-1]+l[i-2])
for i in l:
    print(i,end=' ')