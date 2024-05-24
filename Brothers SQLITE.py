
#==================================================
#Empresa BROTHERS BLOCK
#Programadores - Gabriel, Mário, Nelson e Ryan - Data 30/04/2024
#Programa: Software CRUD da empresa BROTHERS BLOCK
#==================================================

import os
import inquirer
import sqlite3

amarelo = '\033[33m'
verde = '\033[32m'
azul = '\033[34m'
fim = '\033[0m'

# Funções do banco de dados

def consulta_db(): #Consulta retorna um dicionário
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

def criar_db(cod, nome, quant, preco): #Cria um item no SQLite
    with sqlite3.connect("sqlite.db") as conexao:
        cursor = conexao.cursor()
        # Em baixo, ta exatamente igual no pdf
        cursor.execute("INSERT INTO dados (código, material, quantidade, preço) VALUES (?, ?, ?, ?)", (cod, nome, quant, preco))
        conexao.commit() # Commit dos crias

def deletar_db(cod): #Deleta um item pelo código
     with sqlite3.connect("sqlite.db") as conexao:
          cursor = conexao.cursor()
          cursor.execute(f"DELETE FROM dados where código = '{cod}'") # Deleta de dados onde código == cod
          conexao.commit() # Commit dos crias

def alterar_db(cod, nome, quant, preco): #Altera um item no SQLite
     with sqlite3.connect("sqlite.db") as conexao:
          cursor = conexao.cursor()
          cursor.execute(f"UPDATE dados set material = '{nome}' where código ='{cod}'") # Muda material pra nome onde código é cod
          cursor.execute(f"UPDATE dados set quantidade = '{quant}' where código ='{cod}'") # Muda material pra quant onde código é cod
          cursor.execute(f"UPDATE dados set preço = '{preco}' where código ='{cod}'") # Muda preco pra quant onde código é cod
          conexao.commit() # Commit dos crias

# Funções de interface

def confirmação(mensagem): #Confirmação pra continuar
    pergunta_conf = [inquirer.List("opt", message=mensagem, choices=["Sim", "Não"], )]
    conf = inquirer.prompt(pergunta_conf)
    return conf

def preencher_row(cod, nome, quant, valor, cor): #Printa a tabela do produto que está a preencher
        vazio = ''
        print(f'{cor}{vazio:_^88}{fim}')
        print(f"{cor}|{' '*20} |{' '*20} |{' '*20} |{' '*20}|{fim}")
        print(f"{cor}|{fim}{'Código':^20} {cor}|{fim}{'Nome':^20} {cor}|{fim}{'Quantidade':^20} {cor}|{fim}{'Preço':^20}{cor}|{fim}")
        print(f"{cor}|{'_'*20}_|{'_'*20}_|{'_'*20}_|{'_'*20}|{fim}")
        print(f"{cor}|{' '*20} |{' '*20} |{' '*20} |{' '*20}|{fim}")
        print(f"{cor}|{cod:^20} |{nome:^20} |{quant:^20} |{'R$'+str(valor):^20}|{fim}")
        print(f"{cor}|{'_'*20}_|{'_'*20}_|{'_'*20}_|{'_'*20}|{fim}\n")

def tabela(var): #Printa a tabela
    vazio = ''
    print(f'{azul}{vazio:_^88}{fim}')
    print(f"{azul}|{' '*20} |{' '*20} |{' '*20} |{' '*20}|{fim}")
    print(f"{azul}|{fim}{'Código':^20} {azul}|{fim}{'Nome':^20} {azul}|{fim}{'Quantidade':^20} {azul}|{fim}{'Preço':^20}{azul}|{fim}")
    print(f"{azul}|{'_'*20}_|{'_'*20}_|{'_'*20}_|{'_'*20}|{fim}")
    print(f"{azul}|{' '*20} |{' '*20} |{' '*20} |{' '*20}|{fim}")
    for chave,dados in var.items():
        print(f"{azul}|{chave:^20} |{dados[0]:^20} |{dados[1]:^20} |{'R$'+str(dados[2]):^20}|{fim}")
        if chave == list(var.keys())[-1]:  # Verifica se a chave é a última do dicionário
            print(f"{azul}|{'_'*20}_|{'_'*20}_|{'_'*20}_|{'_'*20}|{fim}")
        else:
            print(f'{azul}|{vazio:_^20}_|{vazio:_^20}_|{vazio:_^20}_|{vazio:_^20}|{fim}')
            print(f"{azul}|{' '*20} |{' '*20} |{' '*20} |{' '*20}|{fim}")

def singleRow(cod, cor): #Printa a linha de um produto só
    vazio = ''
    print(f'{cor}{vazio:_^88}{fim}')
    print(f"{cor}|{' '*20} |{' '*20} |{' '*20} |{' '*20}|{fim}")
    print(f"{cor}|{fim}{'Código':^20} {cor}|{fim}{'Nome':^20} {cor}|{fim}{'Quantidade':^20} {cor}|{fim}{'Preço':^20}{cor}|{fim}")
    print(f"{cor}|{'_'*20}_|{'_'*20}_|{'_'*20}_|{'_'*20}|{fim}")
    print(f"{cor}|{' '*20} |{' '*20} |{' '*20} |{' '*20}|{fim}")
    print(f"{cor}|{cod:^20} |{Mat[cod][0]:^20} |{Mat[cod][1]:^20} |{'R$'+str(Mat[cod][2]):^20}|{fim}")
    print(f"{cor}|{'_'*20}_|{'_'*20}_|{'_'*20}_|{'_'*20}|{fim}\n")

# Funções da lógica

def incluir(): #Função para o método incluir
    os.system('cls')
    print(f"{azul}Incluir Material{fim}\n")
    chaves = ", ".join(str(key) for key in Mat.keys())
    print(f'{azul}Os códigos que já estão em uso são: {fim}{chaves}\n')
    while True:
        try:
            cod = int(input(f"Insira um novo código para o Material: "))
            if cod in Mat:
                os.system('cls')
                print(f'\n{amarelo}Um produto já se refere a este código\n{fim}')
                conf = confirmação('Deseja tentar novamente?')
                if conf['opt'] == "Não":
                    return
                else:
                    os.system('cls')
                    print(f"{azul}Incluir Material{fim}\n")
                    print(f'{azul}As chaves que já estão em uso são: {fim}{chaves}\n')
            elif cod < 0:
                os.system('cls')
                print(f"{azul}Incluir Material{fim}\n")
                print(f'{azul}As chaves que já estão em uso são: {fim}{chaves}\n')
                print(f'{amarelo}Por favor insira um número positivo\n{fim}')        
            else:
                break
        except ValueError:
            os.system('cls')
            print(f"{azul}Incluir Material{fim}\n")
            print(f'{azul}Os códigos que já estão em uso são: {fim}{chaves}\n')
            print(f'{amarelo}Por favor insira um valor válido\n{fim}')
    os.system("cls")
    print(f"\n{azul}{'INCLUSÃO DE MATERIAL':^88}{fim}\n")            
    preencher_row(cod, '', '', '', azul)  
    nome=input(f"Insira o nome do Material: ")
    os.system('cls')
    print(f"\n{azul}{'INCLUSÃO DE MATERIAL':^88}{fim}\n")            
    preencher_row(cod, nome, '', '', azul)
    while True:  
        try:
            quant = int(input(f"Insira a quantidade: "))
            os.system('cls')
            if quant <= 0:
                os.system('cls')
                print(f"\n{azul}{'INCLUSÃO DE MATERIAL':^88}{fim}\n")
                preencher_row(cod, nome, '', '', azul) 
                print(f'{amarelo}Por favor insira um número positivo\n{fim}')
            else: break
        except ValueError:
            os.system('cls')
            print(f"\n{azul}{'INCLUSÃO DE MATERIAL':^88}{fim}\n")
            preencher_row(cod, nome, '', '', azul) 
            print(f'{amarelo}Por favor insira um valor válido\n{fim}')
    print(f"\n{azul}{'INCLUSÃO DE MATERIAL':^88}{fim}\n")
    preencher_row(cod, nome, quant, '', azul)        
    while True: 
        try:
            valor=float(input(f"Insira o valor do material: "))
            if valor <= 0:
                os.system('cls')
                print(f"\n{azul}{'INCLUSÃO DE MATERIAL':^88}{fim}\n")
                preencher_row(cod, nome, quant, '', azul)
                print(f'{amarelo}Por favor insira um número positivo\n{fim}') 
            else: break
        except ValueError:
            os.system('cls')
            print(f"\n{azul}{'INCLUSÃO DE MATERIAL':^88}{fim}\n")
            preencher_row(cod, nome, quant, '', azul)
            print(f'{amarelo}Por favor insira um valor válido\n{fim}')  

    criar_db(cod, nome, quant, valor)
    
    os.system('cls')
    print(f"\n{azul}{'INCLUSÃO DE MATERIAL':^88}{fim}\n")
    preencher_row(cod, nome, quant, valor, azul)

    print(f'{verde}Material adicionado com sucesso!\n{fim}')
    input('Pressione ENTER para voltar ao menu')

def excluir(): #Função para o método excluir
    os.system('cls')
    print(f"\n{azul}{'EXCLUSÃO DE MATERIAL':^88}{fim}\n")
    tabela(Mat)
    while True:    
        try:
            excluir_item= int(input("\nInsira o codigo do material a ser removido: "))
            if excluir_item not in Mat:
                os.system('cls')
                print(f"\n{azul}{'EXCLUSÃO DE MATERIAL':^88}{fim}\n")
                tabela(Mat)
                print(f'{amarelo}\nO código digitado não se encontra no sistema{fim}\n')
                conf = confirmação('Deseja tentar novamente?')
                if conf['opt'] == "Não":
                    return
                else:
                    os.system('cls')
                    print(f"\n{azul}{'EXCLUSÃO DE MATERIAL':^88}{fim}\n")
                    tabela(Mat)
            else:
                break
        except ValueError:
            os.system('cls')
            print(f"\n{azul}{'EXCLUSÃO DE MATERIAL':^88}{fim}\n")
            tabela(Mat)
            print(f'{amarelo}\nPor favor insira um valor válido{fim}')  

    if excluir_item in Mat:
        print('')
        conf = confirmação(f'{amarelo}Tem certeza que deseja remover?{fim}')
        if conf['opt'] == "Sim":
            deletar_db(excluir_item)
            os.system('cls')
            print(f"\n{azul}{'EXCLUSÃO DE MATERIAL':^88}{fim}\n")
            tabela(Mat)
            print(f"{verde}\nMaterial removido com sucesso!\n{fim}")
        else:
            os.system('cls')
            input("Pressione ENTER para voltar ao menu")
            return             
    else:
        print("\033[31m") 
        print("Código de material não encontrado.")
    
    input("Pressione ENTER para voltar ao menu")

def reserva_de_material(): #Função para o método reserva
    os.system('cls')
    print(f"\n{azul}{'RESERVA DE MATERIAL':^88}{fim}\n")
    tabela(Mat)
    
    while True:
        try:
            cod_material = int(input("\nInsira o código do material que deseja reservar: "))
            if cod_material not in Mat:
                print(f'{amarelo}\nO código digitado não se encontra no sistema{fim}\n')
                conf = confirmação('Deseja tentar novamente?')
                if conf['opt'] == "Não":
                    return
                else:
                    os.system('cls')
                    print(f"\n{azul}{'RESERVA DE MATERIAL':^88}{fim}\n")
                    tabela(Mat)
            else:
                break
        except ValueError:
            os.system('cls')
            print(f"\n{azul}{'RESERVA DE MATERIAL':^88}{fim}\n")
            tabela(Mat)
            print(f'{amarelo}\nPor favor, insira um valor válido{fim}')

    if cod_material in Mat:
        quantidade_disponivel = Mat[cod_material][1]
        os.system('cls')
        print(f"\n{azul}{'RESERVA DE MATERIAL':^88}{fim}\n")
        singleRow(cod_material, azul)
        
        while True:
            try:
                quantidade_reservar = int(input("Insira a quantidade que deseja reservar: "))
                if quantidade_reservar < 1:
                    os.system('cls')
                    print(f"\n{azul}{'RESERVA DE MATERIAL':^88}{fim}\n")
                    singleRow(cod_material, azul)
                    print(f'{amarelo}Por favor, insira um valor positivo\n{fim}')
                else:
                    break
            except ValueError:
                os.system('cls')
                print(f"\n{azul}{'RESERVA DE MATERIAL':^88}{fim}\n")
                singleRow(cod_material, azul)
                print(f'{amarelo}Por favor, insira um valor válido\n{fim}')

        if quantidade_reservar > quantidade_disponivel:
            print("\033[31m") #cor vermelha
            print("Quantidade solicitada excede o estoque disponível.")
            print(f"{azul}") #cor azul
            input("Pressione ENTER para voltar ao menu")
            return
        else:
            Mat[cod_material][1] -= quantidade_reservar
            os.system('cls')
            print(f"\n{azul}{'RESERVA DE MATERIAL':^88}{fim}\n")
            singleRow(cod_material, azul)
            print(f"{verde}Material reservado com sucesso!\n{fim}")
            input('Pressione ENTER para voltar ao menu')
            return
    else:
        print("\033[31m") #cor vermelha
        print("Código de material não encontrado.")
        print(f"{azul}") #cor azul
        input("Pressione ENTER para voltar ao menu")
    print(f"{azul}") #cor azul

def pesquisar(): #Função para o método pesquisa
    os.system('cls')
    print(f"\n{azul}{'PESQUISAR ITENS':^40}{fim}\n")
    pergunta = [
    inquirer.List(
    "opt",
    message='Menu de opções de pesquisa',
    choices=["Pesquisar por código", "Pesquisar por nome", "Mostrar tabela"],
),
]
    opt = inquirer.prompt(pergunta)

    
    if opt['opt']=="Pesquisar por código": # Pesquisa por código do produto
        os.system('cls')
        print(f"\n{azul}{'PESQUISAR ITENS':^88}{fim}\n")
        preencher_row('', '', '', '', azul)
        chaves = ", ".join(str(key) for key in Mat.keys())
        print(f'{azul}Os códigos presentes no sistema são: {fim}{chaves}')
        while True:
            try:
                cod = int(input("\nInsira o codigo do material a ser pesquisado: "))
                if cod not in Mat:
                    os.system('cls')
                    print(f"\n{azul}{'PESQUISAR ITENS':^88}{fim}\n")
                    preencher_row('', '', '', '', azul)
                    chaves = ", ".join(str(key) for key in Mat.keys())
                    print(f'{azul}Os códigos presentes no sistema são: {fim}{chaves}\n')
                    print(f'{amarelo}O código digitado não se encontra no sistema\n{fim}')
                    conf = confirmação('Deseja tentar novamente?')
                    if conf['opt'] == "Não":
                        return
                    else:
                        os.system('cls')
                        print(f"\n{azul}{'PESQUISAR ITENS':^88}{fim}\n")
                        preencher_row('', '', '', '', azul)
                        chaves = ", ".join(str(key) for key in Mat.keys())
                        print(f'{azul}Os códigos presentes no sistema são: {fim}{chaves}')
                else:
                    os.system('cls')
                    print(f"\n{azul}{'PESQUISAR ITENS':^88}{fim}\n")
                    singleRow(cod, azul)
                    break
            except ValueError:
                os.system('cls')
                print(f"\n{azul}{'PESQUISAR ITENS':^88}{fim}\n")
                preencher_row('', '', '', '', azul)
                chaves = ", ".join(str(key) for key in Mat.keys())
                print(f'{azul}Os códigos presentes no sistema são: {fim}{chaves}')
                print(f'{amarelo}\nPor favor insira um valor válido{fim}')
        input('Pressione ENTER para voltar ao menu')    

    elif opt['opt']=="Pesquisar por nome": # Pesquisa por nome do produto
        os.system('cls')
        print(f"\n{azul}{'PESQUISAR ITENS':^88}{fim}\n")
        preencher_row('', '', '', '', azul)
        nome = input('Insira o nome a ser pesquisado: ')
        nome = nome.lower()
        for chave, dados in Mat.items():
            if dados[0].lower() == nome:
                os.system('cls')
                print(f"\n{azul}{'PESQUISAR ITENS':^88}{fim}\n")
                singleRow(chave, azul)
                input('Pressione ENTER para voltar ao menu')
                encontrado = True
                break
        if not encontrado:
            os.system('cls')    
            print(f"\n{azul}{'PESQUISAR ITENS':^88}{fim}\n")
            preencher_row('', '' ,'' ,'', azul)
            print(f"{amarelo}Material não encontrado\n{fim}")   
            input('Pressione ENTER para voltar ao menu')
    elif opt['opt']=="Mostrar tabela": # Mostrar toda a tabela
        os.system('cls')
        print(f"\n{azul}{'PESQUISAR ITENS':^88}{fim}\n")
        tabela(Mat)
        input('\nPressione ENTER para voltar ao menu')
   
def editar(): #Função para o método editar
    os.system('cls')
    print(f"\n{azul}{'EDIÇÃO DE ITENS':^88}{fim}\n")
    tabela(Mat)
    while True:
        try:
            cod= int(input("\nInsira o codigo do material a ser editado: "))
            if cod not in Mat:
                os.system('cls')
                print(f"\n{azul}{'EDIÇÃO DE ITENS':^88}{fim}\n")
                tabela(Mat)
                print(f'{amarelo}\nO código digitado não se encontra no sistema{fim}\n')
                conf = confirmação('Deseja tentar novamente?')
                if conf['opt'] == "Não":
                    return
                else:
                    os.system('cls')
                    print(f"\n{azul}{'EDIÇÃO DE ITENS':^88}{fim}\n")
                    tabela(Mat)
            else:
                break
        except ValueError:
            os.system('cls')
            print(f"\n{azul}{'EDIÇÃO DE ITENS':^88}{fim}\n")
            tabela(Mat)
            print(f'{amarelo}\nPor favor insira um valor válido{fim}') 
    os.system('cls')
    print(f"\n{azul}{'EDIÇÃO DE ITENS':^88}{fim}\n")        
    singleRow(cod, azul)
    print(f"{verde}\n{'Este item passará a ser:':^88}{fim}")
    preencher_row(cod, '', '', '', verde)
    nome = input('\nInsira um novo nome para o item: ')
    os.system('cls')
    print(f"\n{azul}{'EDIÇÃO DE ITENS':^88}{fim}\n")
    singleRow(cod, azul)
    print(f"{verde}\n{'Este item passará a ser:':^88}{fim}")
    preencher_row(cod, nome, '', '', verde)
    while True:
        try:
            quant = int(input(f"Insira a quantidade: "))
            os.system('cls')
            if quant <= 0:
                os.system('cls')
                print(f"\n{azul}{'EDIÇÃO DE ITENS':^88}{fim}\n")
                singleRow(cod, azul)
                print(f"{verde}\n{'Este item passará a ser:':^88}{fim}")
                preencher_row(cod, nome, '', '', verde)
                print(f'{amarelo}\nPor favor insira um número positivo\n{fim}')
            else: break
        except ValueError:
            os.system('cls')
            print(f"\n{azul}{'EDIÇÃO DE ITENS':^88}{fim}\n")
            singleRow(cod, azul)
            print(f"{verde}\n{'Este item passará a ser:':^88}{fim}")
            preencher_row(cod, nome, '', '', verde)
            print(f'{amarelo}\nPor favor insira um valor válido\n{fim}')
    os.system('cls')
    print(f"\n{azul}{'EDIÇÃO DE ITENS':^88}{fim}\n")
    singleRow(cod, azul)
    print(f"{verde}\n{'Este item passará a ser:':^88}{fim}")
    preencher_row(cod, nome, quant, '', verde)
    while True: 
        try:
            valor=float(input(f"Insira o valor do material: "))
            if valor <= 0:
                os.system('cls')
                print(f"\n{azul}{'EDIÇÃO DE ITENS':^88}{fim}\n")
                singleRow(cod, azul)
                print(f"{verde}\n{'Este item passará a ser:':^88}{fim}")
                preencher_row(cod, nome, quant, '', verde)
                print(f'{amarelo}\nPor favor insira um número positivo\n{fim}') 
            else: break
        except ValueError:
            os.system('cls')
            print(f"\n{azul}{'EDIÇÃO DE ITENS':^88}{fim}\n")
            singleRow(cod, azul)
            print(f"{verde}\n{'Este item passará a ser:':^88}{fim}")
            preencher_row(cod, nome, quant, '', verde)
            print(f'{amarelo}\nPor favor insira um valor válido\n{fim}')
    os.system('cls')
    print(f"\n{azul}{'EDIÇÃO DE ITENS':^88}{fim}\n")
    singleRow(cod, azul)
    print(f"{verde}\n{'Este item passará a ser:':^88}{fim}")
    preencher_row(cod, nome, quant, valor, verde)
    alterar_db(cod, nome, quant, valor)
    print(f"{azul}\n{'Item alterado com sucesso':^88}{fim}")
    input('\nPressione ENTER para voltar para o MENU')
            
while True: #Lógica da escolha
   questions = [
    inquirer.List(
        "opt",
        message='Escolha uma opção',
        choices=["Incluir Item", "Pesquisar Itens", "Excluir Material", "Editar Material", "Reservar Material", "Sair"],
    ),
]
   os.system('cls')
   print(f"{azul}") #cor azul
   print('''
    ██████╗ ██████╗  ██████╗ ████████╗██╗  ██╗███████╗██████╗ ███████╗    ██████╗ ██╗      ██████╗  ██████╗██╗  ██╗
    ██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝██║  ██║██╔════╝██╔══██╗██╔════╝    ██╔══██╗██║     ██╔═══██╗██╔════╝██║ ██╔╝
    ██████╔╝██████╔╝██║   ██║   ██║   ███████║█████╗  ██████╔╝███████╗    ██████╔╝██║     ██║   ██║██║     █████╔╝
    ██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══██║██╔══╝  ██╔══██╗╚════██║    ██╔══██╗██║     ██║   ██║██║     ██╔═██╗
    ██████╔╝██║  ██║╚██████╔╝   ██║   ██║  ██║███████╗██║  ██║███████║    ██████╔╝███████╗╚██████╔╝╚██████╗██║  ██╗
    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝    ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝\n''')
   Mat = consulta_db()
   opt= inquirer.prompt(questions)
   if opt['opt']=="Incluir Item":
       incluir()
   elif opt['opt']=="Pesquisar Itens":
       pesquisar()
   elif opt['opt']== "Reservar Material":
       reserva_de_material()       
   elif opt['opt']=="Excluir Material":
        excluir()
   elif opt['opt'] == "Editar Material":
       editar()                    
   elif opt['opt']== "Sair":
       os.system('cls')
       print(f"{azul}Saindo...{fim}")
       break
