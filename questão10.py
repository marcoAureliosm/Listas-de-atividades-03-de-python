valor1=float(input("INFORME O VALOR DO 1ª PRODUTO"))
valor2=float(input("INFORME O VALOR DO 2ª PRODUTO"))
valor3=float(input("INFORME O VALOR DO 3ª PDRADUTO"))
menor=0
if valor1<valor2 and valor1<valor3:
    menor=valor1
elif valor2<valor1 and valor2<valor3:
    menor=valor2
elif valor3<valor1 and valor3<valor3:
    menor=valor3

print("O PRODUTO QUE VC DEVE COMPRAR É",menor)
