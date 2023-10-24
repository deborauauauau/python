for _ in range(3):
    nome = input("Qual seu nome?")
    nota1 = float(input('Informe a nota 1: '))
    nota2 = float(input('Informe a nota 2: '))
    nota3 = float(input('Informe a nota 3: '))
    nota4 = float(input('Informe a nota 4: '))
    media = (nota1 + nota2 + nota3 + nota4 / 4)
    print (f'A média do aluno {nome} é {media:.2f}')
