# Ex 0 for
n1 = int(input("Digite onde começar: "))
n2 = int(input("Digite onde acabar: "))
n3 = int(input("digite a regra: "))
for x in range(n1,n2 + 1,n3):
    if x <= 0 :
        print("1")
    else : 
        print(x)


# Ex 1 for:
x = int(input("Digite quantas notas são: "))
nota = 0
for media in range(x):
    y = int(input("Digite o valor das notas: "))   
    nota+=y
media = nota/x
print("media: ",media)

# Ex 3 for:
n = 10
soma = 0
for _ in range(n):
    n1 = int(input("Digite os valores: "))
    soma+=n1
media = soma/10
print(media)

# Ex 1 lista: 
lista = [20,40,30,10,0]
lista.sort(reverse=True)
print(lista)

del lista[2]
print(lista[2])

lista[3] = 2
print (lista)

len(lista)
print(len(lista))

# Ex 2 lista:
L = [5,1,3,4,6,7,0]
#a)
L.sort(reverse=True)
print(L)
#b)
L.append(2)
L.append(4)
print(L)
#C)
len(L)
print(L)
#d)
L[0]
#e)
print(L.count(4))
#f)
del L[2]
L.insert(2,10)
#g)
print(L)

# Ex 3 lista:
p = [1,2,3,4,5]
sum(p)
print(sum(p))

# Ex 4 lista:
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))
d = int(input("Digite o quarto valor: "))
e = int(input("Digite o quinto valor: "))
LI = [a,b,c,d,e]
media = (a + b + c + d + e)/5
print(media)
print(a + c)

# Ex 1 while:
x = int(input("Digite um valor: "))
soma = 0
notas = 0
while x >= 0 :
    soma+= x
    notas+=1
    x = int(input("digite um valor: "))
if x == -1:
    media = soma/ notas
    print(media)


# Ex 2 while:
maior = 0
menor = 0
y = int(input("forneça um numero: "))
while y > 0 :
    y = int(input("forneça um numero: "))
    if y > maior :
        maior = y
    if y < menor :
        menor = y
    if y == -1:
        print(maior)
        print(menor)
        break

# Ex 3 while:
soma = 0
valores = 0
z = int(input("insira o valor: "))
while z > 0 :
    z = int(input("insira o valor: "))
    soma+=z
    valores+=1 
if z <= 0 :
    media = soma/valores
    print(media)
    

# Ex 4 while:
maior = 0
qtd = 0
n = int(input("Digite a nota: "))
while n > -1:
    n = int(input("Digite a nota: "))
    if n > maior:
     maior = n
     qtd = 1
    elif n == maior :
     qtd +=1
if n == -1:
    print(maior,qtd+1)

        


