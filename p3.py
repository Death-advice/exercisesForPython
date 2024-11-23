def triangle(a,b,c):
    d=a+b+c
    e=max(a,b,c)
    if d-e>e:
        if a==b==c:
            print("三角形存在，且为等边三角形")
        else:
            print("三角形存在，且为普通三角形")
    else:
        print("三角形不存在")


a,b,c=map(float,input("请输入三角形的边长(用空格隔开三边的边长):").split())
triangle(a,b,c)