f=str(input())
a=len(f[::-1])
l=[]
v=[]
w=[]
for i in range(0,a):
    l.append([f[i+1:],len(f[i+1:])])
    v.append([len(f[i+1:]),f[i+1:]])
l.sort()
v.sort()
l=max(l)
v=max(v)
w.append(l[0])
w.append(v[1])
w.append(f[0])
l=[]
for i in w:
    if(i[0]>f[0]):
        l.append(i)
print(sorted(l)[0])
