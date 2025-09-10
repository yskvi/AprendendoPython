# Arrae - armazenar várias informações em uma varíavel

# PRIMEIRO EXEMPLO
# nomes = ["lavinia", "Sofia", "nathaly", "charlie"]
# print(nomes[3])

#SEGUNDO EXEMPLO
# numeroCliente = int(input("Quantos clientes você quer cadastrar? "))
# clientes = []
# vetor = [0 for i in range(numeroCliente)]
# for i in range(numeroCliente):
#  clientes.insert(i, input("Digite o nome do cliente: "))
# print(clientes)
# clientes.pop(2)
# print(clientes)

#TERCEIRO EXEMPLO
# clientes = [["Lavs", "Sofia", "nat"], [15, 100, 10], ["Verde", "Preto", "Rosa"]]
# print(clientes[0][1])
# print(clientes[1][1])
# print(clientes[2][1])

# QUARTO EXEMPLO
# numeroCliente = int(input("Quantos clientes você quer cadastrar? "))
# vetor = [0 for i in range(numeroCliente)]
# for i in range(numeroCliente):
#     print(f"\n digite os dados da pessoa: {i}")
#     nome = input("nome: ")
#     idade = int(input("idade: "))
#     sexo = input("sexo: ")

#     vetor[i] = {
#     "nome": nome,
#     "idade": idade,
#     "sexo": sexo
#     }

# # print("\n  lista de pessoas cadastradas")
# # for pessoas in vetor:
# #     print(pessoas)

# outra forma dessa parte
# print()
# print(vetor[0] ["nome"])

# EXEMPLO 5
# from random import randint
# computador = randint (0, 5)
# print(computador)

# Jogo
from random import randint
computador = randint (0, 10)
numero = int(input("Adivinhe o número que a máquina escolheu! Escolha um número entre 0 a 10: "))
if numero == computador:
    print("Você acertou!")

else:
  print(f"Você errou! a máquina escolheu {computador}")