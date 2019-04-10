qhoras=float(input("QUANTO VC GANHA POR HORAS"))
horas=int(input("QUANTAS HORAS VC TRABALHA"))
bruto=qhoras*horas
cinco=(5/100.0)*bruto
dez=(10/100.0)*bruto
vinte=(20/100.0)*bruto
onze=(11/100.0)*bruto
if bruto<=900:
    print("Seu salario bruto é de :",bruto-cinco)
    print("(-)IR(5%)","R$",cinco)
    print("(-)INSS(10%)","R$:",dez)
    print("FGTS(11%):","R$",onze)
    print("Total desconto","R$",cinco+dez+onze)
elif bruto>=900 and bruto>1500:
    print("Seu salario bruto é de :",bruto-dez)
    print("(-)IR(5%)","R$",cinco)
    print("(-)INSS(10%)","R$:",dez)
    print("FGTS(11%):","R$",onze)
    print("Total desconto","R$",cinco+dez+onze)
elif bruto>1500:
    print("Seu salario bruto é de :",bruto-vinte)
    print("(-)IR(5%)","R$",cinco)
    print("(-)INSS(10%)","R$:",dez)
    print("FGTS(11%):","R$",onze)
    print("Total desconto","R$",cinco+dez+onze)
