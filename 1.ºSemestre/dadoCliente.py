valor_compra = input("Informe o valor da compra realizada ")
cupom = input("digite o cupom de desconto ")

if cupom.upper() == "NIVER10":
    valor_compra = float(valor_compra) * 0.9
else:
    valor_final = float(valor_compra)
    print("CUPOM INVÁLIDO")
print("O valor final da compra é {}".format(valor_final))

