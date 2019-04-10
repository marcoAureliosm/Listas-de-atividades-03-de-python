n1=int(input("DIGITE UM VALOR"))
n2=int(input("DIGITE OUTRO VALOR"))
n3=int(input("DIGITE OUTRO VALOR"))
maior=0
menor=0
if n1 > n2  and n1 > n3:
    maior=n1

    if n2 < n3:
        menor=n2
    else:
        menor=n3
if n2 > n3 and n2 > n1:
    maior = n2
    if n3 < n1:
        menor = n3
    else:
        menor = n1
if n3 > n2 and n3> n1:
    maior = n3
    if n2 < n1:
        menor = n2
    else:
        menor = n1



print("Maior valor {} Menor valor {}".format(maior,menor))