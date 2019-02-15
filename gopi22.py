#gopi
n=int(input())
x=list(map(int,input().split()))
if (len(x)==n):
    print(max(x))
else:
    print("The range of array is invalid")
