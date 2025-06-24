email_aluno = input("Informe o email do aluno")
nota_semestral = input("Informe a nota semestral do aluno: ")

nota_semestral = float(nota_semestral)

if nota_semestral > 8.5:
    print("ENVIANDO E-MAIL PARA {}".format(email_aluno))

