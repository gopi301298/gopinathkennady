#gopi
n,k=map(int,input().split())
for a in range (n,k+1):
    v=0
    for i in range (2,a//2+1):
        if(a%i==0):
            v=v+1
    if(v<=0):
        print(a)
