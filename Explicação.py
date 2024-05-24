import sqlite3
azul = '\033[34m'
fim = '\033[0m'
amarelo = '\033[33m'

# "dados" é o banco de dados

def consulta_db():
    Mat = {}
    with sqlite3.connect("sqlite.db") as conexao:
            cursor = conexao.cursor() # No pdf ta com with, mas pra min funcionou assim
            cursor.execute("SELECT * FROM dados") # Seleciona tudo de dados
            rows = cursor.fetchall() # O método busca todas (ou todas as linhas restantes) de um conjunto de resultados de consulta e retorna uma lista de tuplas. // Definição do site do MySQL
            # Inclusive ta no pdf também
            if rows: # Confere se não ta vazio
                for row in rows: # Seleciona cada row, numa iteração
                    Mat[row[0]] = [row[1], row[2], row[3]] # Transforma no dicionário
    return Mat

Mat = consulta_db()
print(f"\n{azul} Primeiro Mat - Só a consulta\n {fim}{Mat}\n")

input(f'{amarelo}Aperta enter pra ir pra criação{fim}')

def criar_db(cod, nome, quant, preco):
    with sqlite3.connect("sqlite.db") as conexao:
        cursor = conexao.cursor()
        # Em baixo, ta exatamente igual no pdf
        cursor.execute("INSERT INTO dados (código, material, quantidade, preço) VALUES (?, ?, ?, ?)", (cod, nome, quant, preco))
        conexao.commit() # Commit dos crias

criar_db(4, "papel", 42, 64)

Mat = consulta_db()
print(f"\n{azul} Segundo Mat - Deve aparecer papel\n {fim}{Mat}\n")

input('Aperta enter pra ir pra exclusão')

# Nada novo, no pdf amigos
def deletar_db(cod):
     with sqlite3.connect("sqlite.db") as conexao:
          cursor = conexao.cursor()
          cursor.execute(f"DELETE FROM dados where código = '{cod}'") # Deleta de dados onde código == cod
          conexao.commit() # Commit dos crias

deletar_db(4)

Mat = consulta_db()
print(f"\n{azul} Terceiro Mat - Papel sumiu\n {fim}{Mat}\n")

input('Aperta enter pra ir pra alteração')

def alterar_db(cod, nome, quant, preco):
     with sqlite3.connect("sqlite.db") as conexao:
          cursor = conexao.cursor()
          cursor.execute(f"UPDATE dados set material = '{nome}' where código ='{cod}'") # Muda material pra nome onde código é cod
          cursor.execute(f"UPDATE dados set quantidade = '{quant}' where código ='{cod}'") # Muda material pra quant onde código é cod
          cursor.execute(f"UPDATE dados set preço = '{preco}' where código ='{cod}'") # Muda preco pra quant onde código é cod
          conexao.commit() # Commit dos crias

alterar_db(1, "Alumínio", 10, 43)

Mat = consulta_db()
print(f"\n{azul} Quarto Mat - Madeira agora é alumínio \n {fim}{Mat}\n")

input('Aperta enter pra ir pra alteração')

with sqlite3.connect("sqlite.db") as conexao:
     cursor = conexao.cursor()
     cursor.execute(f"UPDATE dados set material = 'Madeira' where código ='1'") # Muda material pra nome onde código é cod
     cursor.execute(f"UPDATE dados set quantidade = '100' where código ='1'") # Muda material pra nome onde código é cod
     cursor.execute(f"UPDATE dados set preço = '180' where código ='1'") # Muda material pra nome onde código é cod

          