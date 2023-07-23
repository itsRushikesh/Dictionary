def funint(a,b):
    if 4-b and (b and a) < a+b :
        a= 2+a+b
        b= a+2
        b = 2+a+b
        return a+funint(a,a)
    a = 3+2+a
    return a+b


print(funint(2,17))