a,b,c=map(float,input("请分别输入a，b，c（用空格隔开三个参数）：").split())
if a!=0:
    delta=b*b-4*a*c
    if delta>0:
        x1=(-b-delta*0.5)/2*a
        x2=(-b+delta*0.5)/2*a
        print(x1,x2)
    elif delta==0:
        x1=x2=(-b)/2*a
        print(f"x1=x2={x1}")
    else:
        print("此方程无实根")
else:
    print("这不是一个一元二次方程！")