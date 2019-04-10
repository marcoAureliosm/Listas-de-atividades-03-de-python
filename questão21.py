dia=int(input("DIGITE O DIA"))
mes=int(input("DIGITE O MES"))
ano=int(input("DIGITE O ANO"))
if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
    if (dia <= 31):
        print("DATA VALIDA")
        print("{}/{}/{}".format(dia,mes,ano))
    else:
        print('DATA INVALIDA')
        print("{}/{}/{}".format(dia, mes, ano))

    # Meses com 30 dias
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    if (dia <= 30):
        print("DATA VALIDA")
        print("{}/{}/{}".format(dia, mes, ano))
    else:
        print('DATA INVALIDA')
        print("{}/{}/{}".format(dia, mes, ano))
elif mes == 2:
    # Testa se é bissexto
    if (ano % 4 == 0 and ano % 400 != 0) or (ano % 400 == 0):
        if (dia <= 29):
            print("DATA VALIDA")
            print("{}/{}/{}".format(dia, mes, ano))
        else:
            print('DATA INVALIDA')
            print("{}/{}/{}".format(dia, mes, ano))
    elif (dia <= 28):
        print("DATA VALIDA")
        print("{}/{}/{}".format(dia, mes, ano))
    else:
        print('DATA INVALIDA')
        print("{}/{}/{}".format(dia, mes, ano))



