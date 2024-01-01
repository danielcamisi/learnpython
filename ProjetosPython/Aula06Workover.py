nome=input("Digite seu nome: ")
nome=str(nome)
idade=input("Digite sua idade: ")
idade=int(idade)
renda=input("Digite sua renda: ")
renda=float(renda)

if renda >= 2000:
    print(nome,"! Seu crédito foi aprovado")
else:
    print(nome,"! Seu crédito não foi aprovado, sua renda deve ser maior ou igual a R$2000.00")