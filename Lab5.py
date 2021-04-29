import random
'''
print("1.Faça um programa que leia nome e média de um aluno guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.")

nome = input("Digite o seu nome")
media = float(input("Digite a sua média"))

if (media >= 6):
    situ = 'Aprovado'

else:
    situ = 'Reprovado'

dici = {nome, media, situ}

print(dici)

print("2.Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em uma lista. No final, coloque essa lista em ordem, sabendo que o vencedor tirou o maior número no dado.")

jogadores = []
jogadores_dados = []
maior_j = []
x = 0
maior = 0

for x in range(4):
    nome = input('Digite o seu nome')
    jogadores += [nome,]
    dado = random.randint(1,6)
    jogadores_dados += [dado,]

print(jogadores)
print(jogadores_dados)

for y in range(3):
    for x in range(3):
        if(jogadores_dados[x] >= jogadores_dados[x+1]):
            aux = jogadores_dados[x]
            aux1 = jogadores[x]
            jogadores_dados[x] = jogadores_dados[x+1] 
            jogadores[x] = jogadores[x+1]
            jogadores_dados[x+1] = aux
            jogadores[x+1] = aux1

print(jogadores)
print(jogadores_dados)

for x in range (4):
    if(maior == jogadores_dados[x]):
        maior_j += [jogadores[x]]
    if(maior < jogadores_dados[x]):    
        maior = jogadores_dados[x]
        maior_j = [jogadores[x]]
    
print("O jogador que tirou o maior número foi o ", maior_j, "tirou: ", maior)

print("3.Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule  e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.")

trab = {}
trab['nome'] = input("Digite o nome ")
trab['ano_nasc'] = input("Digite o ano de nascimento")
trab['carteira_trab'] = input("Digite a sua carteira de trabalho")

if(trab['carteira_trab'] != '0'):
    trab['ano_contra'] = input("Digite o ano em que foi contratado")
    trab['salario'] = input("Digite o seu salário")

contratacao = int(trab['ano_contra'])
contribuicao = 2021 - contratacao
x = int(trab['ano_nasc'])

contri_apo = 20 - contribuicao
idade = 2021 - x

anos_apo = 85 - (idade + contri_apo) 
anos_apo = idade + anos_apo

trab['anos_apo'] = anos_apo
trab['idade'] = idade
print(trab)

print("4.Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:")

i = int(input("Digite o número de pessoas que irá cadastrar"))
paciente = [] 
pacientes = []
pesadas = []
leves = []

for x in range (i):
    pacientes.append(str(input("Digite o nome")))
    pacientes.append(float(input("Digite o peso")))
    if len(paciente) == 0:
        maior = menor = pacientes[1]
    else:
        if pacientes[1] > maior:
            maior = pacientes[1]
        if pacientes[1] < menor:
            menor = pacientes[1]
    paciente.append(pacientes[:])
    pacientes.clear()

print(f"Foram cadastradas {i} pessoa(s)")
print(f"O maior peso foi: {maior}, e o menor foi {menor}")

for x in paciente:
    if x[1] == maior:
        pesadas += [x[0]]
        
print(f"As pessoas mais pesadas são: {pesadas}, com {maior} Kg")

for x in paciente:
    if x[1] ==  menor:
        leves += [x[0]]

print(f"As pessoas mais leves são: {leves}, com {menor} Kg")
'''
print("5. Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os \
    em uma lista única que mantenha separados os valores pares e ímpares. \
        No final, mostre os valores pares e ímpares em ordem crescente.")

principal = [[], []]

for x in range (8):
    num = int(input("Digite um número"))
    if num % 2 == 0:
        principal[0].append(num)
    else:
        principal[1].append(num)

principal[0].sort()
principal[1].sort()

print(f"Os valores pares são:{principal[0]}")
print(f"Os valores impares são:{principal[1]}")