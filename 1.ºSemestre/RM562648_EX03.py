divida = float(input("Digite o valor da dívida:"))

opcoes = [(1, 0), (3, 10), (6, 15), (9, 20), (12, 25)]

for parcelas, juros in opcoes:
    valor_juros = divida * (juros / 100)
    total = divida + valor_juros
    valor_parcela = total / parcelas
    print(f"Total:R$ {total:.2f} Juros:R$ {valor_juros:.2f} Número de parcelas:{parcelas} Valor da Parcela:R$ {valor_parcela:.2f}")