n=int(input())
n1=2**n
for i in range(0,n1):
    l=bin(i)[2:].zfill(n)
    print(l)
    
