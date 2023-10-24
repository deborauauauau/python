while True:
    valor_compra = float("Informe o valor da compra:  ")
    if valor_compra <= 1500.00:
        percentual_desconto = 5

    elif valor_compra <= 2000.00:
        percentual_desconto = 10
    
    elif valor_compra <= 3000.00:
        percentual_desconto = 15
    
    else:
        percentual_desconto = 20

    desconto = (valor_compra * percentual_desconto)/100

    print(f"O valor da compra antes do deaconto: ", {valor_compra})
    print(f"O percentual de desconto aplicado: ", {percentual_desconto})
    print(f"O valor do desconto é de: ", {desconto})
    print(f"O valor a ser pago após o desconto: ", {valor_compra - desconto})

    continuar = input("Deseja continuar? s/n")
    if continuar.lower() != "s":
        break