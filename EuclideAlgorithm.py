m,n=map(int,input().split())

def gcd(a,b):
    while b!=0:
        c=a
        a=b
        b=c%a
    return a
m1=str(m//gcd(m,n))
n1=str(n//gcd(m,n))
print(m1+"/"+n1)