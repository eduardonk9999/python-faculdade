votos = {}
dias_validos = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]

num_colaboradores = int(input("Informe o número de colaboradores: "))

for i in range(num_colaboradores):
    while True:
        voto = input("Informe o dia da sua preferência (segunda-feira, terça-feira, quarta-feira, quinta-feira, sexta-feira): ").lower()
        if voto in dias_validos:
            votos[voto] = votos.get(voto, 0) + 1
            break
        else:
            print("Dia inválido. Tente novamente.")

mais_votado = max(votos.values())
dias_ganhadores = [dia for dia, qtd in votos.items() if qtd == mais_votado]

if len(dias_ganhadores) > 1:
    print(f"Houve empate entre os dias: {', '.join(dias_ganhadores)}")
else:
    print(f"O dia escolhido pelos colaboradores é: {dias_ganhadores[0]}")