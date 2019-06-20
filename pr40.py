s=str(input())
l=['d','h','o','n','i']
c=0
for i in range(len(s)):
    if(s[i] in l):
        c=c+1
if(c-len(s)==0):
    print("yes")
else:
    print("no")
