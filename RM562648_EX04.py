print("Escolha o tipo de investimento:\n1. CDB\n2. LCI\n3. LCA")
tipo = int(input("Digite o tipo de investimento (1, 2 ou 3): "))

if tipo not in [1, 2, 3]:
    print("Tipo de investimento inválido!")
else:
    valor = float(input("Digite o valor a ser resgatado: "))
    dias = int(input("Digite o número de dias que o valor permaneceu investido: "))

    if tipo == 1:  # CDB
        if dias <= 180:
            aliquota = 0.225
        elif dias <= 360:
            aliquota = 0.20
        elif dias <= 720:
            aliquota = 0.175
        else:
            aliquota = 0.15
        imposto = valor * aliquota
        print(f"O valor do imposto de renda a ser pago é: R$ {imposto:.2f}")
    else:
        print("Este tipo de investimento é isento de imposto de renda.")