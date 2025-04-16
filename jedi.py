#criação de uma lista com os nomes dos Jedi
jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
#incluindo um valor digitado no final da lista
jedi.append(input("Digite o nome de um jedi"))
#A variável assumirá cada um dos valores da lista
for nome in jedi:
    #para cada volta do loop, exibir o valor assumido
    print(nome)

# jedi.pop => remove o último item da lista.
# count() => retorna a quantidade de vezes que um elemento aparece na lista.
# sort() => organiza a lista em ordem crescente/alfabética.
# reverse() => inverte a ordem dos elementos de uma lista.