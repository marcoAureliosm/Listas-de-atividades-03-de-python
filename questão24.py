aluno1=int(input("DIGITE SUA IDADE"))
aluno2=int(input("DIGITE UMA IDADE"))
aluno3=int(input("DIGITE UMA IDADE"))
if aluno1 < 25 and aluno2 < 25 and aluno3 < 25:
    print("TURMA JOVEN")
elif aluno1>25 and aluno1<40 and aluno2>25 and aluno2<40 and aluno3>25 and aluno3<40:
    print("TURMA ADULTA")
elif aluno1>40 and aluno2 >40 and aluno3>40:
    print("TUMAR IDOSA")