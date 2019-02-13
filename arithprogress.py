#gopi
n,a,d=map(int,input().split())
c=0
g=0
while(c<n):
    g=(a+c*d)+g
    c=c+1
print(g)
