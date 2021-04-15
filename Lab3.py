print('1.Crie um programa que leia o nome completo de uma pessoa e mostre:')
nome = input('Digite o seu nome')

print('a) O nome com todas as letras maiúsculas e minúsculas')
print(nome.upper())
print(nome.lower())

print('b) Quantas letras ao todo(sem considerar espaços)')
nome1 = nome.replace(" ", "")
q = len(nome1)
print('O número de caracteres no nome é:', q)

print('c) Quantas letras tem o primeiro nome')
nome = nome.split()
nome2 = nome[0]
q = len(nome2)
print('O número de caracteres no primeiro nome é:', q)

val = 0

print('2.Escreva um programa que leia o comprimento de 3 retas e diga ao usuário se ela podem ou não formar um triângulo.')
n1 = int(input('Digite o primeiro número'))
n2 = int(input('Digite o segundo número'))
n3 = int(input('Digite o terceiro número'))

if n1 >= n2 and n1 >= n3:
    maior = n1
    soma = n2 + n3
    if soma >= maior:
        print('O triangulo é possível')
        val = 1
    else:
        print('O triangulo não é possivel')
if n2 > n1 and n2 > n3:
    maior = n2
    soma = n1 + n3
    if soma >= maior:
        print('O triangulo é possível')
        val = 1
    else:
        print('O triangulo não é possivel')
if n3 > n1 and n3 > n2:
    maior = n3
    soma = n1 + n2
    if soma >= maior:
        print('O triangulo é possível')
        val = 1
    else:
        print('O triangulo não é possivel')

print('3. Crie uma questão usando a matéria dada na aula com o gabarito.')
print('Para complementar a questão anterior, faça o programa descobrir qual é o tipo do triangulo')
if val == 1:
    if n1 == n2 and n1 == n3:
        print('Esse é um triangulo retangulo')
    if n1 == n2 and n2 != n3:
        print('Esse é um triangulo Isósceles')
    if n2 == n3 and n3 != n1:
        print('Esse é um triangulo Isósceles')
    if n3 == n1 and n1 != n2:
        print('Esse é um triangulo Isósceles')    
    if n1 != n2 and n2 != n3 and n3 != n1:
        print('Esse é um triangulo Escaleno')    
else:
    print('O triangulo não é possivel')