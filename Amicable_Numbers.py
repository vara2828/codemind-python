def proper_factor_sum(num):
    pfs=0
    for i in range(1,num):
        if num%i==0:
            pfs+=i
    return pfs

a=int(input())
b=int(input())
if proper_factor_sum(a)==b and proper_factor_sum(b)==a:
    print("Amicable")
else:
    print("Not Amicable")
