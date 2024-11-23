def func(x):
    if x>1:
        y=x+5
    elif -1<=x<=1:
        y=x*x+2
    else:
        y=x-10
    return y


x=float(input("请输入x："))
print(func(x))