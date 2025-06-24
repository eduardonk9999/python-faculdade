
valorBrutoPacode = float(input("Valor Bruto do pacote "))
passageiros = float(input("Digite quantas passagens voce pretende comprar "))
categoriaAssentos = input("Econômica, Executiva ou Primeira classe ")

if categoriaAssentos == 'Econômica':
    print("Valor bruto".format(valorBrutoPacode))
    if passageiros == 2:
        desconto = valorBrutoPacode * (2 / 100)
        print("Seu valor bruto: {}".format(valorBrutoPacode))
        print("Seu desconto é: {}".format(desconto))
    elif passageiros == 3:
        desconto = valorBrutoPacode * (4 / 100)
        print("Seu valor bruto: {}".format(valorBrutoPacode))
        print("Seu desconto é: {}".format(desconto))
    elif passageiros >= 4:
        desconto = valorBrutoPacode * (5 / 100)
        print("Seu valor bruto: {}".format(valorBrutoPacode))
        print("Seu desconto é: {}".format(desconto))
    else:
        desconto = 0

if categoriaAssentos == 'Executiva':
    print("Valor bruto".format(valorBrutoPacode))
    if passageiros == 2:
        desconto = valorBrutoPacode * (5 / 100)
        print("Seu valor bruto: {}".format(valorBrutoPacode))
        print("Seu desconto é: {}".format(desconto))
    elif passageiros == 3:
        desconto = valorBrutoPacode * (7 / 100)
        print("Seu valor bruto: {}".format(valorBrutoPacode))
        print("Seu desconto é: {}".format(desconto))
    elif passageiros >= 4:
        desconto = valorBrutoPacode * (8 / 100)
        print("Seu valor bruto: {}".format(valorBrutoPacode))
        print("Seu desconto é: {}".format(desconto))
    else:
        desconto = 0

if categoriaAssentos == 'Primeira classe':
    print("Valor bruto".format(valorBrutoPacode))
    if passageiros == 2:
        desconto = valorBrutoPacode * (10 / 100)
        print("Seu valor bruto: {}".format(valorBrutoPacode))
        print("Seu desconto é: {}".format(desconto))
    elif passageiros == 3:
        desconto = valorBrutoPacode * (15 / 100)
        print("Seu valor bruto: {}".format(valorBrutoPacode))
        print("Seu desconto é: {}".format(desconto))
    elif passageiros >= 4:
        desconto = valorBrutoPacode * (20 / 100)
        print("Seu valor bruto: {}".format(valorBrutoPacode))
        print("Seu desconto é: {}".format(desconto))
    else:
        desconto = 0