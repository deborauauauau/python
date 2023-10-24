n = 1
while n<= 3:
    salario_atual = float(input("Digite o salário do funcionário: "))

    if salario_atual<= 1500.00:
        percentual_aumento = 20
    elif salario_atual<= 2000.00:
        percentual_aumento=15
    elif salario_atual<= 3000.00:
        percentual_aumento=10
    else:
        percentual_aumento=5

    aumento = (salario_atual*percentual_aumento)/100
    novo_salario = salario_atual + aumento

    print (f"Salário antes do reajuste: R$ {salario_atual}") 
    print (f"Percentual de aumento aplicado: {percentual_aumento}")
    n= n+1