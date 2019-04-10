nome=str(input("Digite seu nome"))
nota1=float(input("Digite sua 1ª nota"))
nota2=float(input("Digite sua 2ª nota"))
soma=(nota1+nota2)/2
if soma> 3.0:
    print("{} você está reprovado sua media foi :{}".format(nome,soma))
elif soma<3 and soma >=7:
    print("{} você está de exame sua media foi :{}".format(nome, soma))
elif soma<=7 and soma ==10:
    print("{} você está aprovado sua media foi :{}".format(nome, soma))
