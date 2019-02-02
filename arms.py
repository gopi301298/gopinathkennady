#gopi
n=int(input())
summ=0
temp=n
while(temp>0):
    digit=temp%10
    summ+=digit**3
    temp//=10
if n==summ:
    print("Yes")
else:
    print("No")
