print('[1]DOMINGO\n [2]SEGUNDA\n [3]TERÇA\n [4]QUARTA\n [5]QUINTA\n [6]SEXTA\n [7]SABADO')
dia=int(input("DIGITE O SEU DIA DA SEMANA"))
if dia == 1 :
    print('DOMINGO')
elif dia==2:
    print('SEGUNDA')
elif dia==3:
    print('TERÇA')
elif dia==4:
    print('QUARTA')
elif dia==5:
    print('QUINTA')
elif dia==6:
    print('SEXTA')
elif dia==7:
    print('SABADO')
elif dia <=0 and dia <=7:
    print('DIA INVALIDO')

