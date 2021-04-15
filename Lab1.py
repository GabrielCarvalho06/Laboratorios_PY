'''Gabriel da Silva Carvalho
Matricula: 0050013382'''

'''1 Organize os números 2,3,4,5,10,12 para obter a saída 18 em uma única operação.'''

'''2.Escreva um programa que imprima 2 números de sua escolha e que depois imprima a soma, a subtração, multiplicação, divisão,
 divisão inteira, o resto da divisão do maior pelo menor e coloque na mensagem a palavra resto ao invés de símbolo %.'''

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

soma = num1 + num2
print('soma desses numeros é: ', soma)

sub = (num1 - num2)
print('A subtracao desses numeros é: ', sub)

multi = num1 * num2
print('A multiplicacao desses numeros é: ', multi)

divisao = num1 / num2
print('A divisão entre esses numeros é: ', divisao)

'''3. Faça um programa que peça as 4 notas bimestrais e mostre a média do aluno'''

nota1 = float(input('Digite a nota da primeira prova: '))
nota2 = float(input('Digite a nota da segunda prova: '))
nota3 = float(input('Digite a nota da terceira prova: '))
nota4 = float(input('Digite a nota da quarta prova: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(media)

'''4.Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
 Calcule e mostre o total do seu salário no referido mês'''

vhora = float(input('Digite o valor da sua hora: '))
qtdhora = float(input('Digite o numero de horas trabalhadas durante o mês: '))

salario = vhora * qtdhora

print(salario)

'''5.Crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de Boas Vindas de acordo
 com o valor digitado.'''

nome = input('Digite seu nome: ')
print('Seja bem vindo ', nome)

'''6. Crie um script Python que leia o dia, mês e ano de nascimento de uma pessoa e mostre uma mensagem
 com a data formatada.'''

dia = input('Digite o dia em que você nasceu: ')
mes = input('Digite o mes em que você nasceu: ')
ano = input('Digite o ano em que você nasceu: ')

print('Você nasceu em: '+dia+'/'+mes+'/'+ano)

'''7.Crie um script Python que leia o preço de um produto e mostre seu novo preço com 5% de desconto.'''
preco = float(input('Digite o valor do produto: '))
print('Aplicando desconto')
novop = preco * 0.95
print(f'O preco com desconto é: {novop:.2f}')

'''8.Crie um script Python que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento'''

salario = float(input('Digite o valor do seu salário: '))
print('Calculando aumento')
novos = salario * 1.15
print(f'O salario com aumento é: {novos:.2f}')

'''9.Crie um script Python que converta uma temperatura digitada em graus Celsius para Fahrenheit.'''
celcius = float(input('Digite a temperatura em celcius que voce deseja converter: '))
fahrenheit = (celcius * 1.8) + 32
print('A conversao em fahrenheit é: ', fahrenheit)

'''10.Crie um script Python que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
 Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por KM rodado.'''

km = float(input('Quantos quilometros você andou? '))
dias = float(input('Quantos dias voce ficou com o carro? '))

vkm = km * 0.15
vdias = dias * 60
total = vkm + vdias
print('O valor total a ser pago é de ', total, 'reais')