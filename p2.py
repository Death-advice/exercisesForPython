def oddsum(n):
    s=0
    for i in range(0,n+1):
        if i%2==0:
            s+=i
    return s


print(oddsum(100))