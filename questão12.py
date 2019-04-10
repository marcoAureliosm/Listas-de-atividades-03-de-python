salario=float(input("DIGITE O SEU SALARIO: "))
if salario <= 280.0:
    total=(salario*(20/100))+salario
elif salario >= 280.0 and salario <= 700.0:
    total = (salario * (15 / 100)) + salario
elif salario >= 700.0 and salario <=1500.0:
    total = (salario * (10 / 100)) + salario
elif salario >=1500.0:
    total = (salario * (5 / 100)) + salario
print("O SEU SALARIO REAJUSTADO FICOU : ",total)


