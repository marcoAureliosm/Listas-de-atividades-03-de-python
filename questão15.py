custo=float(input("DIGITE O CUSTO DO PRODUTO"))
origen=int(input("DIGITE O CODIGO DE ORIGEM DO PRODUTO"))
if origen==1:
    origen="Sul"
    print("VALOR DO PRODUTO:{} E SUA ORIGEM: {}".format(custo,origen))
elif origen==2:
    origen = "Norte"
    print("VALOR DO PRODUTO:{} E SUA ORIGEM: {}".format(custo, origen))
elif origen==3:
    origen = "Leste"
    print("VALOR DO PRODUTO:{} E SUA ORIGEM: {}".format(custo, origen))
elif origen==4:
    origen = "Oeste"
    print("VALOR DO PRODUTO:{} E SUA ORIGEM: {}".format(custo, origen))
elif origen==5 or origen==6:
    origen = "Nordeste"
    print("VALOR DO PRODUTO:{} E SUA ORIGEM: {}".format(custo, origen))
elif origen==7 or origen==8:
    origen = "Centro - Oeste"
    print("VALOR DO PRODUTO:{} E SUA ORIGEM: {}".format(custo, origen))
else:
    origen = "Internacional"
    print("VALOR DO PRODUTO:{} E SUA ORIGEM: {}".format(custo, origen))
