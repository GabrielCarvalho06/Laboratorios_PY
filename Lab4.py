import random
from datetime import data1, data2


print ("1. Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um numero pelo teclado(entre 0 e 20) e mostra-lá por extenso.")

numerost = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

xt = int(input("Digite um número de zero a vinte"))

print(numerost[xt])

print("2. Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:")

timest = ('Flamengo', 'Internacional', 'Atlético - MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos', 'Atlético - PR', 'Red Bull Bragantino', 'Ceará', 'Corinthians', 'Atlético - GO', 'Bahia', 'Sport', 'Fortaleza', 'Vasco', 'Goiás', 'Coritiba', 'Botafogo')
print(timest)
print("Os cinco primeiros colocados:")

x = 0
for x in range(5):
    if (x < 5):
        print(timest[x])

print("Os últimos 4 colocados da tabela:")

for x in range(20):
    if (x > 15):
        print(timest[x])

print("Uma lista com os times em ordem alfabética.")
timesl = sorted(timest)

print(timesl)

print("Em que posição na tabela está o time do Vasco")
for x in range (20):
    if (timest[x] == 'Vasco'):
        print("O vasco está na ", x+1, "posição da tabela")

print("3.Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.")
maior = 0
menor = 10000
numero = ()
y = 0
x = type(numero)
print(x)

for x in range (5):
    y = random.randint(0, 9999)
    numero += (y,)

print(numero)
for x in range(5):
    if(maior < numero[x]):
        maior = numero[x]
    if(menor > numero[x]):
        menor = numero[x]
    
        
print(maior)
print(menor)


print("4.Crie um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:")

numero1 = ()
print("Digite quatro números")
for x in range (4):
    y = input("Escolha o número")
    numero1 += (y,)

print(numero1)
for x in range (4):
    v = int(numero1[x])
    c = numero1.count('9')
    resto = (v % 2)
    if(resto == 0):
        print("O número", numero1[x], "é par")
    else:
        print("O número", numero1[x], "não é par")
    
print("O número 9 aparece", c, "vezes")
print("O 3 encontra-se na posição: ", numero1.index('3')+1)


print("5. Faça um programa que calcule o número de dias corridos entre duas datas, para vários pares de datas, considerando a possibilidade de ocorrência de anos bissextos, sendo que: A primeira data é sempre a mais antiga; O ano é fornecido com 4 dígitos; A data fornecida com ZERO dias é o sinal para encerrar a entrada de dados")

#Resposta do gabarito

from datetime import datetime

def diferenca_dias(d1, d2):
        d1 = datetime.strptime(date1, "%d/%m/%Y")
        d2 = datetime.strptime(d2, "%d/%m/%Y")
        return abs((d2 - d1).days)

soma = 0

print('*****Digite "0" em um dos dias para encerrar!******')
print('***********Padrão de data: 20/11/2015************')

d1 = input("\nDigite o dia mais antigo:")
m1 = input('Digite o mês mais antigo:')
a1 = input('Digite o ano mais antigo:')

d2 = input("\nDigite o dia mais recente:")
m2 = input('Digite o mês mais recente:')
a2 = input('Digite o ano mais recente:')

date1 = d1 + '/' + m1 + '/' + a1
date2 = d2 + '/' + m2 + '/' + a2

while d1 != '0' and d2 != '0':

    soma = soma + diferenca_dias(date1, date2)
    
    print('\n\nTemos ' , soma, ' dias corridos no total.')

    print('\n\n\nDigite 0 em um dos dias para encerrar!')
    print('Padrão de data: 20/11/2015')

    d1 = input("\nDigite o dia mais antigo:")
    m1 = input('Digite o mês mais antigo:')
    a1 = input('Digite o ano mais antigo:')

    d2 = input("\nDigite o dia mais recente:")
    m2 = input('Digite o mês mais recente:')
    a2 = input('Digite o ano mais recente:')

else:
    print('\n\n*****O programa foi encerrado!*****')

    
from datetime import datetime # Resposta do Israel

dt_in=1
while dt_in != '0':
    dt_in = input(str('Digite a data incial (ex.: 1/1/2021): '))
    if dt_in != '0':
        dt_fn = input(str('Digite a data final (ex.: 31/12/2021): '))
        a = dt_in.split('/')
        b = dt_fn.split('/')
        if len(a[2]) < 4 or len(b[2]) < 4:
            print('Ano invalido.')
            break
        dt_in = datetime.strptime(dt_in, '%d/%m/%Y')
        dt_fn = datetime.strptime(dt_fn, '%d/%m/%Y')

        if dt_in > dt_fn:
            print('Data inicial superior a data final, erro')
            break
        else:
            dias = dt_fn - dt_in
            print(dias.days)
    else:
        continue