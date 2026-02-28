#Exercício 1
# x = input("Digite o nome do usuario: ")
# y = int(input("Digite a senha do usuario: "))
# if x == "admin" and y == 1234:
#     print("Acesso permitido")
# elif x == "user" and y == "abcd":
#     print("Acesso permitido")
# else:    print("Acesso negado")

#Exercício 2
# import random

# # Gera um número aleatório entre 1 e 100
# numero_secreto = random.randint(1, 100)

# print("Jogo de Adivinhação!")
# print("Tente adivinhar o número entre 1 e 100.")

# while True:
#     try:
#         palpite = int(input("Digite seu palpite: "))
        
#         if palpite < numero_secreto:
#             print("📉 O número secreto é MAIOR que o seu palpite.")
#         elif palpite > numero_secreto:
#             print("📈 O número secreto é MENOR que o seu palpite.")
#         else:
#             print("🎉 Parabéns! Você acertou o número!")
#             break

#     except ValueError:
#         print(" Por favor, digite um número válido.")


#Exercício 3
# def maior_numero(a, b):
#     if a > b:
#         return a
#     else:
#         return b


# # Exemplo de uso
# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))

# resultado = maior_numero(num1, num2)
# print("O maior número é:", resultado)

#Exercício 4
# def numero_primo(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# # Exemplo de uso
# num = int(input("Digite um número: "))

# if numero_primo(num):
#     print(num, "é um número primo.")
# else:    print(num, "não é um número primo.")

#Exercício 5
# def calcular_media(lista):
#     if len(lista) == 0:
#         return 0  # Evita divisão por zero
#     return sum(lista) / len(lista)


# # Exemplo de uso
# numeros = [10, 20, 30, 40, 50]
# media = calcular_media(numeros)

# print("A média é:", media)

#Exercício 6
