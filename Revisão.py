#Entrada e Saida e operações

#Exercicio 1
# Crie um programa que peça o nome do usuario e mostre:

# nome = input("Digite seu nome: ")
# print("Olá, " + nome + " seja bem vindo ao python.")

#Exercicio 2
#Peça dois números ao usuário e mostre:# Soma # Subtração # Multiplicação # Divisão

# n1 = int(input("Digite o primeiro numero: "))
# n2 = int(input("Digite o segundo numero: "))
# print("Soma = " + str(n1 + n2))
# print("Subtração = " + str(n1 - n2))
# print("Multiplicação = " + str(n1 * n2))
# print("Divisão = " + str(n1 / n2))

#Exercicio 3
#Peça um número e diga se ele é par ou ímpar.
# n = int(input("Digite um número: "))
# if n % 2 == 0:
#     print("O número é par.")
# else:
#     print("O número é ímpar.")

#Exercicio 4
#Peça a idade do usuário e diga se ele é:
#Menor de idade
#Maior de idade
# idade = int(input("Digite sua idade: "))
# if idade < 18:
#     print("Você é menor de idade.")
# else:    print("Você é maior de idade.")

#Exercicio 5
#Peça a temperatura em Celsius e converta para Fahrenheit.
# celsius = float(input("Digite a temperatura em Celsius: "))
# fahrenheit = (celsius * 9/5) + 32
# print("A temperatura em Fahrenheit é: ", fahrenheit)

#CONDIÇÕES E REPETIÇÕES

#Exercicio 6
#Peça uma senha ao usuário, e Continue pedindo até ele digitar "1234".
# Senha = ""
# while Senha != "1234":
#     Senha = input("Digite a senha: ")
# print("Senha correta!")

#Exercicio 7
#Mostre todos os números de 1 até 100 usando for.
# for i in range(1,101):
#     print(i)

#Exercicio 8
#Mostre apenas os números pares de 1 até 50.
# for i in range(1,51):
#     if i % 2 == 0:
#        print(i)

#Exercicio 9
#Peça 5 números ao usuário e mostre a soma deles.
# Soma = 0
# for i in range(5):
#     n = int(input("Digite um número: "))
#     Soma += n
# print("Soma = " + str(Soma))

#Exercicio 10
#Peça um número e mostre a tabuada dele (de 1 a 10).
# N = int(input("Digite um número: "))
# for i in range(1,11):
#     print(str(N) + " x " + str(i) + " = " + str(N * i))

#FUNÇÕES
#Exercicio 11
#Crie uma função que receba um número e retorne o dobro dele.
# def dobro(n):
#     return n * 2
# print(dobro(5)) # Exemplo de uso da função, deve retornar 10

#Exercicio 12
#Crie uma função que receba dois números e retorne o maior.
# def maior(n1, n2):
#     if n1 > n2:
#         return n1
#     else:
#         return n2
# print(maior(12, 6)) # Exemplo de uso da função, deve retornar 12

#Exercicio 13
#Crie uma função que receba uma lista e retorne a média.
# def media(lista):
#     if len(lista) == 0:
#         return 0
#     return sum(lista) / len(lista)
# # Exemplo de uso da função, deve retornar 5.5
# print(media([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

#Exercicio 14
#Crie uma função que verifique se um número é primo.
# def primo(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# # Exemplo de uso da função, deve retornar True
# print(primo(5)) # Deve retornar True

#LISTAS
#Exercicio 15
#Crie uma lista com 5 números e mostre:
#O maior número
#O menor número
# numeros = [10, 5, 8, 3, 12]
# print("Maior número:", max(numeros))
# print("Menor número:", min(numeros))

#Exercicio 16
#Peça 5 números ao usuário e armazene em uma lista. Depois mostre a lista em ordem crescente.
# numeros = []
# for i in range(5):
#     n = int(input("Digite um número: "))
#     numeros.append(n)
# numeros.sort()
# print("Lista em ordem crescente:", numeros)

#Exercicio 17
#Conte quantas vezes um número aparece dentro de uma lista.
# numeros = [1, 2, 3, 4, 5, 2, 3, 2]
# n = int(input("Digite um número: "))
# print("O número", n, "aparece", numeros.count(n), "vezes na lista.")

#Desafio Extra
#Exercicio 18
#Faça um jogo de adivinhação:
# Gere um número aleatório entre 1 e 100
# O usuário deve tentar adivinhar
# O programa deve dizer se o número é maior ou menor
# import random
# numero_secreto = random.randint(1, 100)
# tentativas = 0
# while True:
#     palpite = int(input("Digite seu palpite (entre 1 e 100): "))
#     tentativas += 1
#     if palpite < numero_secreto:
#         print("O número é maior.")
#     elif palpite > numero_secreto:
#         print("O número é menor.")
#     else:
#         print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
#         break

#Dicionários
#Exercicio 19
#Crie um dicionário com as seguintes informações:
# nome
# idade
# cidade # Depois, mostre cada informação separadamente.
# dicionario = {
#     "nome": "João",
#     "idade": 25,
#     "cidade": "São Paulo"
# }
# print("Nome:", dicionario["nome"])
# print("Idade:", dicionario["idade"])
# print("Cidade:", dicionario["cidade"])

#Exercicio 20
#Crie um dicionário com 3 produtos e seus preços.
# Exemplo:
# {"Arroz": 20, "Feijão": 8, "Macarrão": 5}
# Mostre apenas os preços.
# produtos = {
#     "Arroz": 20,
#     "Feijão": 8,
#     "Macarrão": 5
# }
# for produto, preco in produtos.items():
#     print(f"Produto: {produto}, Preço: {preco}")

#Exercicio 21
# Peça ao usuário:
# nome
# idade
# Guarde em um dicionário e depois mostre:
# Nome:
# Idade:
# usuario = {}
# usuario["nome"] = input("Digite seu nome: ")
# usuario["idade"] = int(input("Digite sua idade: "))
# print("Nome:", usuario["nome"])
# print("Idade:", usuario["idade"])

#Exercicio 22
#Crie um dicionário vazio.
# Adicione 3 chaves depois da criação.
# dicionario = {}
# dicionario["chave1"] = "valor1"
# dicionario["chave2"] = "valor2"
# dicionario["chave3"] = "valor3"
# print(dicionario)

#Exercicio 23
#Dado o dicionário:
# aluno = {"nome": "Carlos", "nota": 7}
# Altere a nota para 9.
# aluno = {"nome": "Carlos", "nota": 7}
# aluno["nota"] = 9
# print(aluno)

#Exercicio 24
#Verifique se a chave "idade" existe em um dicionário.
# Se existir, mostre o valor.
# Se não existir, mostre "Chave não encontrada".
# dicionario = {"nome": "Ana", "cidade": "Rio de Janeiro","idade": 30}
# if "idade" in dicionario:
#     print("Idade:", dicionario["idade"])
# else:
#     print("Chave não encontrada")

#Exercicio 25
#Conte quantas chaves existem em um dicionário.
# dicionario = {"nome": "Ana", "cidade": "Rio de Janeiro", "idade": 30}
# print("Número de chaves no dicionário:", len(dicionario))

#Exercicio 26
#Percorra um dicionário usando for e mostre:
# chave -> valor
# dicionario = {"nome": "Ana", "cidade": "Rio de Janeiro", "idade": 30}
# for chave, valor in dicionario.items():
#     print(f"{chave} -> {valor}")

#Exercicio 27
#Crie um dicionário com nomes de 5 alunos e suas notas.
# Mostre:
# O aluno com maior nota
# A média das notas
# alunos = {
#     "Alice": 8,
#     "Bob": 9,
#     "Charlie": 7,
#     "David": 6,
#     "Eve": 8
# }
# maior_nota = max(alunos.values())
# aluno_maior_nota = [aluno for aluno, nota in alunos.items() if nota == maior_nota]
# print("Aluno(s) com maior nota:", ", ".join(aluno_maior_nota))
# media = sum(alunos.values()) / len(alunos)
# print("Média das notas:", media)

#Exercicio 28
#Crie um sistema simples de cadastro:
# O usuário pode cadastrar 3 pessoas
# Cada pessoa deve ter:
# nome
# idade
# Armazene tudo dentro de um dicionário
# Exemplo de estrutura:
# {
#   "pessoa1": {"nome": "Ana", "idade": 20},
#   "pessoa2": {"nome": "João", "idade": 25}
# }
# cadastro = {}
# for i in range(1, 4):
#     nome = input(f"Digite o nome da pessoa {i}: ")
#     idade = int(input(f"Digite a idade da pessoa {i}: "))
#     cadastro[f"pessoa{i}"] = {"nome": nome, "idade": idade}
# print(cadastro)

#Desafio Extra
#Exercicio 29
#Crie um sistema de estoque simples:
# Peça ao usuário para cadastrar produtos e quantidades.
# Depois pergunte qual produto ele deseja consultar.
# Mostre a quantidade disponível.
# Se não existir, mostre: "Produto não encontrado".
# estouque = {}
# for i in range(3):
#     produto = input(f"Digite o nome do produto {i+1}: ")
#     quantidade = int(input(f"Digite a quantidade do produto {i+1}: "))
#     estouque[produto] = quantidade
# produto_consultado = input("Digite o nome do produto que deseja consultar: ")
# if produto_consultado in estouque:
#     print(f"Quantidade disponível de {produto_consultado}: {estouque[produto_consultado]}")
# else:    print("Produto não encontrado")