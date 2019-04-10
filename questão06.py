n1=int(input("DIGITE UM VALOR"))
n2=int(input("DIGITE UM VALOR"))
n3=int(input("DIGITE UM VALOR"))
if n1 > n2 >n3:
    print(n3, n2, n1)
elif n1>n3>n2:
    print(n1, n3, n2)
elif n2>n1>n3:
    print(n2, n1, n3)
elif n2>n3>n1:
    print(n2, n3, n1)
elif n3>n1>n1:
    print(n3, n1, n2)
elif n3>n2>n1:
    print(n3, n2, n1)
elif n1 == n2 or n1 == n3 or n2 == n3:
    print("INVALIDO")