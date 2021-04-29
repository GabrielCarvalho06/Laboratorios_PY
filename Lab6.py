print("1. Crie uma função que exiba uma saudação com os parâmetros saudação e nome")

def saudacao (nome, sauda):
    print(f"Seja bem vindo {nome}, o {sauda} !!!")

nome = str(input("Digite o seu nome: "))
sauda = str(input("Digite a saudação que você quer para você: "))

saudacao(nome, sauda)


print("2. Crie uma função que receba 3 números como parâmetros e exiba a soma entre eles.")

def soma (num1, num2, num3):
    som = num1 + num2 + num3
    print(f"A soma dos três números é: {som}")

n1 = int(input("Digite o primeiro número"))
n2 = int(input("Digite o segundo número"))
n3 = int(input("Digite o terceiro número"))

soma(n1, n2, n3)

print("3. Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual(ex 10%). \
    Retorne(return) o valor do primeiro numero somado do aumento do percentual do mesmo.")

def soma2 (num, perce):
    num = num * perce
    return(num)

numero = float(input("Digite um número"))
percentual = float(input("Digite o percentual"))
percentual = (percentual / 100) + 1 

print(soma2(numero, percentual))

print("4. Fizz Buzz - Se o parâmetro da função for divisível por 2, retorne fizz, \
    se o parâmetro da função for  divisível por 5 e por 3 , retorne FizzBuzz, \
        caso contrário, retorne o numero enviado. ")

def fizzbuzz (num):
    if num % 2 == 0:
        return 'Fizz'
    if (num % 3 == 0) and (num % 5 == 0):
        return 'FizzBuzz'
    else:
        return(num)

numero = int(input("Digite um número"))

print(fizzbuzz(numero))


print("5. Crie um programa que tenha uma função notas() que pode receber várias notas de alunos \
e vai retornar um dicionário com as seguintes informações: \
a)Quantidade de notas b)A maior nota c) A menor nota d)A média da turma e)A situação (opcional)")

def nota(notas):
    dici = {}
    maior = 0
    menor = 0
    media = 0
    
    dici['cadastrados'] = len(notas)
    for x in range (len(notas)):
        media = media + notas[x]
        if x == 0:
            maior = menor = notas[x]
            print(maior)
            print(menor)
        else:
            if maior < notas[x]:
                maior = notas[x]
            if menor > notas[x]:
                menor = notas[x]
    media = media / len(notas)
    dici['maior'] = maior
    dici['menor'] = menor
    dici['media'] = media
    return(dici)
    

notas = ()
i = 'S'
while i == 'S':
    notas += (float(input("Digite a nota")),)
    i = str(input("Quer digita outra nota? S/N"))

print(nota(notas))

