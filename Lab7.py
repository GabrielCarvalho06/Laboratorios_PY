'''
1.Escreva a função(objetivo) de cada comando abaixo(Banco de dados)

a. import mysql.connector
Importa o modulo do conector do sql.
import mysql.connector

b. cursor
Variável para fazer a utilização do banco de dados.
cursor = conexao.cursor()

c.create database
Cria um novo banco de dados.
cursor.execute('create database ')

d. show databases
Mostra todos os banco de dados do servidor em que está conectado.
cursor.execute('show databases')
for x in cursor:
    print(x)

e. create tables
Cria uma tabela dentro de um banco de dados já existente.
cursor.execute('create table aluno(cod_aluno int(10) primary key AUTO_INCREMENT, nome varchar(40) not null, \
idade int(3), email varchar(50))')

f. show tables
Mostra todas as tabelas dentro de um banco de dados.
cursor.execute('show tables')
for a in cursor:
    print(a)

g. execute
Executa uma função no servidor em que está conectado, com o auxiílio de uma variável 'cursor'.
cursor.execute('')

h. insert into ... values
Atribui dados a uma variável 'sql' e depois executa essa variável no banco de dados, inserindo os dados no banco.
sql = 'INSERT into aluno (nome, idade, email) values ("Gabriel", "27", "gabriel.teste@gmail.com")'

i. commit
Serve para validar as alterações feitas na tabela.
conexao.commit()

j. rowcount
Conta o número de dados executados pela variável cursor em uma tabela do banco.
print(cursor.rowcount, 'registro(s) inserido(s)')

k. executemany
executa mais de uma linha para o banco.
cursor.executemany(sql, val)

l. select
Função do banco de dados para vizualizar os dados de uma tabela no banco.
cursor.execute('SELECT * from aluno')
result = cursor.fetchall()
for x in result:
    print(x)

m. fetchall
função para trazer todas as linhas de uma tabela do banco.
result = cursor.fetchall()

n. where
Serve para determinar uma condição ao que você deseja executar no banco de dados.
cursor.execute('SELECT nome from aluno where idade > 25')
result = cursor.fetchall()
for x in result:
    print(x)

o. delete
Serve para deletar dados de uma tabela do banco.
sql = 'DELETE from aluno where nome = "Lorenna"'
cursor.execute(sql)
conexao.commit()
print(cursor.rowcount, 'Registo(s) deletado(s)')

p.drop table
Serve para deletar uma tabela inteira do banco.
cursor.execute('drop table aluno')

q.update
Serve para atualizar dados em uma tabela do banco.
sql = 'UPDATE aluno set nome = "Gabriel da Silva Carvalho" where cod_aluno = 2'
cursor.execute(sql)
conexao.commit()
print(cursor.rowcount, 'Registo(s) atualizados(s)')

r. limit
Limita o número de dados trazidos da tabela no banco.
cursor.execute('SELECT * from aluno limit 5')
result = cursor.fetchall()
for x in result:
    print(x)

s. offset
Serve para dizer a partir de onde a variável vai trazer os dados da tabela.
cursor.execute('SELECT * from aluno limit 5 offset 2')
result = cursor.fetchall()
for x in result:
    print(x)

t. between
Serve para buscar dados do banco em um intervalo entre os registros.
cursor.execute('select * FROM tabela WHERE idade BETWEEN 20 and 30')
'''

import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = ''
)

cursor = conexao.cursor()
print(conexao)

cursor.execute('create database lista7')

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'lista7'
)
cursor = conexao.cursor()
print(conexao)

cursor.execute('create table aluno(cod_aluno int(10) primary key AUTO_INCREMENT, nome varchar(40) not null, \
    endereco varchar(200), telefone varchar(20), email varchar(50), cpf varchar(15))')

cursor.execute('create table professor(cod_prof int(10) primary key AUTO_INCREMENT, nome varchar(40) not null, \
    endereco varchar(200), telefone varchar(20), email varchar(50), carga_horaria float(5))')

sql = 'INSERT into aluno (nome, endereco, telefone, email, cpf) values(%s, %s, %s, %s, %s)'
val = [
    ("Daiana", "Rua teste", "(21) 999899765", "teste1@gmail.com", "15899265874"),
    ("Lucas", "Rua teste", "(21) 995674123", "teste2@gmail.com", "15899265874"),
    ("Vitor", "Rua teste", "(21) 999899765", "teste3@gmail.com", "15899265874"),
    ("Josiane", "Rua teste", "(21) 995674123", "teste4@gmail.com", "15899265874"),
    ("Amanda", "Rua teste", "(21) 999899765", "teste5@gmail.com", "15899265874"),
]
cursor.executemany(sql, val)
print(cursor.rowcount, 'registro(s) inserido(s)')

sql = 'INSERT into professor (nome, endereco, telefone, email, carga_horaria) values(%s, %s, %s, %s, %s)'
val = [
    ("Thereza Pratos", "Rua teste", "(21) 999899765", "teste1@gmail.com", "240"),
    ("Alex Salgado", "Rua teste", "(21) 995674123", "teste2@gmail.com", "220"),
    ("Mario joão", "Rua teste", "(21) 999899765", "teste3@gmail.com", "180"),
    ("Marcia Sadok", "Rua teste", "(21) 995674123", "teste4@gmail.com", "190"),
    ("Fabio barros", "Rua teste", "(21) 999899765", "teste5@gmail.com", "230"),
]
cursor.executemany(sql, val)
print(cursor.rowcount, 'registro(s) inserido(s)')

sql = 'UPDATE professor set nome = %s where cod_prof = %s'
cursor.execute(sql,('Thereza Prado', 1))
print(cursor.rowcount, 'Registo(s) atualizado(s)')

cursor.execute('SELECT * from professor')
result = cursor.fetchall()
for x in result:
    print(x)

conexao.commit()
conexao.close()