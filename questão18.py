lado1=int(input("Digite o lado do triangulo"))
lado2=int(input("Digite o lado do trinagulo"))
lado3=int(input("Digite o lado do triangulo"))
if (lado1 <= lado2 + lado3):
    print('formar um triangulo')

    if (lado1 == lado2 == lado3):
        print('triangulo eqüilátero')

    elif (lado1 == lado2 != lado3) or (lado1 == lado3 != lado2) or (lado2 == lado3 != lado1):
        print('triangulo Isosceles')

    elif (lado1 != lado2 != lado3):
        print('Triangulo escaleno')
    else:
        print('Não é um triangulo')


