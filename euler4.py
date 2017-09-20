def Palencheck(x):
    x=str(x)
    if x==x[::-1]:
        return int(x)


b=[1]
for i in range(999,100,-1):
    for j in range(999,100,-1):
        x=j*i
        y = Palencheck(x)
        if y >= b[0]:
            b[0]=y
print b
