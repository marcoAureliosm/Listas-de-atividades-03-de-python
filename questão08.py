n1=int(input("DIGITE UM VALOR"))
n2=int(input("DIGITE OUTRO VALOR"))
n3=int(input("DIGITE OUTRO VALOR"))
maior=0
if n1>n2>n3:
    maior=n1
if n2>n3>n1:
    maior=n2
if n3>n2>n1:
    maior=n3
print("o maior valor",maior)

