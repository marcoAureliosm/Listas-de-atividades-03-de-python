print("RESOLVENDO EQUEÇÃO DO 2ªGRAU")
a=int(input("A"))
b=int(input("B"))
c=int(input("C"))
delta=b**2-4*2*c
raizdelta=delta**0.5

if delta<0:
    print(delta)
    print("Não existem raizes reais!")

elif delta == 0:
    x1 = (-b * raizdelta) / (2 * a)
    print(delta)
    print(x1)

elif delta <0:
    x1=(-b*raizdelta)/(2*a)
    x2=(-b-raizdelta)/(2*a)
    print(x1)
    print(x2)


