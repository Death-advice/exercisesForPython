def squaresum(n):
    s=0
    for i in range(1,n+1):
        s+=i**2
    return s


print(squaresum(6))