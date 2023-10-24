
while True:
    nome = input(" Informe seu nome: ")
    nota1 = float(input(nome+ " Informe a primeira nota:"))
    nota2 = float(input(nome+ " Informe a segunda nota:"))
    nota3 = float(input(nome+ ' Informe a terceira nota:'))
    nota4 = float(input(nome+ ' Informe a quarta nota:'))
    freq =  float(input(nome+ " Informe o percentual de frequência: "))
    media = (nota1 + nota2 + nota3 + nota4)/4

    if media>=7 and freq>=75:
     print (f"O aluno(a) {nome} foi aprovado(a) com média {media:.1f} e frequência de {freq} %")
    elif media >=5 and freq>=50: 
        print (f"O aluno está em recuperação {media:.1f} e frequência de {freq:.1f} % ")
        nota_rec = float(input(nome + " Informe a nota da recuperação: "))
        nova_med = (media + nota_rec)/2
        print(f"A nova média do aluno(a) {nome} após a recuperação é {nova_med:.1f} ")
        if nova_med >=6:
         print (f"O aluno {nome} foi aprovado com a média de {nova_med:.1f}")

        else:
         print (f"O aluno(a) {nome} foi reprovado(a) com média {media:.1f} e frequência de {freq:.1f} %")
    else:
        print (f"O aluno foi reprovado com média {nova_med}")

    continuar = input("Deseja continuar? (s/n)")
    if continuar.lower() != "s":
       break


