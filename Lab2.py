'''Gabriel da Silva Carvalho
Matricula: 0050013382'''

print('1.Faça um programa que sortei um numero de 0 a 9999 e mostre na tela cada um dos dígitos separadamente.exemplo: unidade: 4 dezena: 3 centena: 8 milhar')
import random
r = random.randint(0 , 9999)
print(r)

print('2.Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o numero escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.')

r = random.randint(0 , 5)
print('SPOILER', r)
x = int(input('Digite um número entre 0 e 5 e tente adivinhar o número que foi escolhido'))
if x == r:
    print('Parabéns, você acertou!!!')
else:
    print('Você errou!!!')

print('3.Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada KM acima do limite.')
vel = int(input('Qual a velocidade?'))
print(vel)

if vel > 80:
    print('Está acima do limite de velocidade')
    multa = vel - 80
    multa = multa * 7
    print('O valor da multa é de', multa, 'reais.')
else:
    print('Está dentro do limite de velocidade')

print('4.Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200Km e R$0,45 para viagens mais longos.')
dist = float(input('Digite a distancia da viagem'))
print(dist)

if dist <= 200:
    val = dist * 0.5
    print('O valor da passagem é de R$', val)
else:
    val = dist * 0.45
    print('O valor da passagem é de R$', val)
print('5.Faça um programa que leia um ano qualquer e mostre se ele é Bissexto.')
ano = int(input('Digite o ano'))
print(ano)

resto = ano % 4
print('Resto = ', resto)

if resto == 0:
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')

print('6.Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.')
n1 = int(input('Digite o primeiro número'))
n2 = int(input('Digite o segundo número'))
n3 = int(input('Digite o terceiro número'))

if n1 > n2 and n1 > n3:
    maior = n1
    maior1 = ('Primeiro número')
    if n2 > n3:
        menor = n3
        menor1 = ('Terceiro número')
    else:
        menor = n2
        menor1 = ('Segundo número')
    print('O maior número é: ', maior,maior1, 'E o menor número é: ', menor,menor1)
if n2 > n1 and n2 > n3:
    maior = n2
    maior1 = ('Segundo número')
    if n1 > n3:
        menor = n3
        menor1 = ('Terceiro número')
    else:
        menor = n1
        menor1 = ('Primeiro número')
    print('O maior número é: ', maior,maior1, 'E o menor número é: ', menor,menor1)
if n3 > n1 and n3 > n2:
    maior = n3
    maior1 = ('Terceiro número')
    if n1 > n2:
        menor = n2
        menor1 = ('Segundo número')
    else:
        menor = n1
        menor1 = ('Primeiro número')
    print('O maior número é: ', maior,maior1, 'E o menor número é: ', menor,menor1)

print('7.Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o numero é de 15%.')
sal = float(input('Digite o valor do seu salário'))
print(sal)

if sal > 1250:
    sal = sal * 1.1
else:
    sal = sal * 1.15
print(f'O novo salário é R$: {sal:.2f}')