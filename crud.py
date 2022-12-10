import mysql.connector
from termcolor import colored
from time import sleep
import os

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="programacao"
)

def main():

  def countdown(t):

   while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        sleep(1)
        t -= 1

  while True:
    os.system("cls")
    print("""
  =========================
  | 1: Create             |
  | 2: Read               |
  | 3: Update             |
  | 4: Delete             |
  =========================
  | 5: Criar Database     |
  | 6: Mostar Databases   |
  | 0: Sair               |
  =========================

  """)

    entrada = int(input('Escolha uma opção: '))

    if entrada == 1:
        mycursor = mydb.cursor()
        nome = str(input('Digite o nome da Linguagem: '))
        criado = str(input('Quando foi criado: '))
        valor = (f'"{nome}", "{criado}"')
        sql = (f"INSERT INTO linguagens (nome, criado) VALUES ({valor})")
        mycursor.execute(sql)
        mydb.commit()
        print(colored("Cadastrado com sucesso.", 'green'))
    elif entrada == 2:
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM linguagens")
        myresult = mycursor.fetchall()
        print('='*25)
        print('|', '  Nome  ', '|', '  Criado  ', '|')
        for linha in myresult:
                print('='*25)
                print('|  ', linha[1], '|  ', linha[2], '    |')
                print('='*25)
        read = int(input('Digite 1 para voltar: '))
        if read == 1:
            t = 5
            print('Voltando em')
            countdown(int(t))
            main()
    elif entrada == 3:
        print('1 = Nome')
        print('2 = Criado')
        update = int(input('Digite uma opção para modificar: '))
        if update == 1:
         numero = int(input('Qual o ID da tabela: '))
         novo_nome = str(input('Digite o Novo Nome: '))
         sql = (f"UPDATE linguagens SET nome = '{novo_nome}' WHERE id = '{numero}'")
        else:
         numero = int(input('Qual o ID da tabela: '))
         novo_criado = str(input('Digite o Novo Nome: '))
         sql = (f"UPDATE linguagens SET criado = '{novo_criado}' WHERE id = '{numero}'")
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        mydb.commit()
        print(colored("Modificado com sucesso.", 'green'))
        sleep(5)
    elif entrada == 4:
        print('Digite uma opção para excluir: ')
        num = int(input('Qual o ID da tabela: '))
        sql = (f"DELETE FROM linguagens WHERE id = {num}")
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        mydb.commit()
        print(colored("Removido com sucesso.", 'green'))
        sleep(5)

    elif entrada == 5:
        database1 = str(input('Digite o nome do banco de dados: '))
        mycursor = mydb.cursor()
        mycursor.execute(f"CREATE DATABASE {database1}")
        print(colored("Banco de dados criado com sucesso.", 'green'))
    elif entrada == 6:
        mycursor = mydb.cursor()
        mycursor.execute("SHOW DATABASES")
        for x in mycursor:
            bd = str(x)[1:-1].replace("'", "").replace(",", "")
            print('Database:', bd)

    elif entrada == 0:
        exit()

main()
