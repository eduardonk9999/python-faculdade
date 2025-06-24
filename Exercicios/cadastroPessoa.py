nome = input("Seu nome: ")
idade = input("Sua idade: ")

pessoa = {
    "nome": nome,
    "idade": idade
}

print(f"Olá, {pessoa['nome']}")