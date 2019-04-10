nota1=float(input("Digite sua 1ª nota"))
nota2=float(input("Digite sua 2ª nota"))
soma=(nota1+nota2)/2
if soma <=9.0 and soma>=10.0:
    print("Sua media é:{} [A] APROVADO SUA NOTA : 1ª{} 2ª{}".format(soma,nota1,nota2))
elif soma<=7.5 and soma>=9.0:
    print("Sua media é:{} [B] APROVADO SUA NOTA : 1ª{} 2ª{}".format(soma,nota1,nota2))
elif soma<=6 and soma >=7.5:
    print("Sua media é:{} [C] APROVADO SUA NOTA : 1ª{} 2ª{}".format(soma,nota1,nota2))
elif soma<=4.0 and soma>=6.0:
    print("Sua media é:{} [D] REPROVADO SUA NOTA : 1ª{} 2ª{}".format(soma,nota1,nota2))
elif soma <4.0:
    print("Sua media é:{} [E] REPROVADO SUA NOTA : 1ª{} 2ª{}".format(soma,nota1,nota2))


