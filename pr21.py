import statistics as st
a=int(input())
l=list(map(int,input().split()))
c=0
for i in range(1,a):
    l1=l[0:i]
    l2=l[i:a]
    if(st.mean(l1)==st.mean(l2)):
        c=c+1
if(c>=1):
    print("yes")
else:
    print("no")
