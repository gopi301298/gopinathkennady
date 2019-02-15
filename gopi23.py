#gopi
n=int(input())
x=list(map(int,input().split()))
if (len(x)==n):
    print(min(x))
else:
    print("The range of array is invalid")
