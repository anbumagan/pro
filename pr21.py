import statistics as st
a=int(input())
l=list(map(int,input().split()))
c=0
for i in range(1,a):
    l1=l[0:i]
    print(l1)
    l2=l[i:a]
    print(l2)
    if(st.mean(l1)==st.mean(l2)):
        c=c+1
if(c>=1):
    print("yes")
else:
    print("no")
