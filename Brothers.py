#==================================================
#Empresa BROTHERS BLOCK
#Programadores - Gabriel, Mário, Nelson e Ryan - Data 30/04/2024
#Programa: Software CRUD da empresa BROTHERS BLOCK
#==================================================
import os
from pprint import pprint
import inquirer

Mat={
100:["Madeira", 100, 180],
101:["Ferro", 100, 125],
102:["Tijolo", 100, 3.30],
}

amarelo = '\033[33m'
verde = '\033[32m'
azul = '\033[34m'
fim = '\033[0m'

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

def tabela(): # Printa a tabela
    vazio = ''
    print(f'{azul}{vazio:_^88}{fim}')
    print(f"{azul}|{' '*20} |{' '*20} |{' '*20} |{' '*20}|{fim}")
    print(f"{azul}|{fim}{'Código':^20} {azul}|{fim}{'Nome':^20} {azul}|{fim}{'Quantidade':^20} {azul}|{fim}{'Preço':^20}{azul}|{fim}")
    print(f"{azul}|{'_'*20}_|{'_'*20}_|{'_'*20}_|{'_'*20}|{fim}")
    print(f"{azul}|{' '*20} |{' '*20} |{' '*20} |{' '*20}|{fim}")
    for chave,dados in Mat.items():
        print(f"{azul}|{chave:^20} |{dados[0]:^20} |{dados[1]:^20} |{'R$'+str(dados[2]):^20}|{fim}")
        if chave == list(Mat.keys())[-1]:  # Verifica se a chave é a última do dicionário
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

def incluir():
    os.system('cls')
    vazio = ''
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

    Mat[cod]=[nome,quant,valor]
    os.system('cls')
    print(f"\n{azul}{'INCLUSÃO DE MATERIAL':^88}{fim}\n")
    preencher_row(cod, nome, quant, valor, azul)

    print(f'{verde}Material adicionado com sucesso!\n{fim}')
    input('Pressione ENTER para voltar ao menu')

def excluir(): 
    os.system('cls')
    print(f"\n{azul}{'EXCLUSÃO DE MATERIAL':^88}{fim}\n")
    tabela()
    while True:    
        try:
            excluir_item= int(input("\nInsira o codigo do material a ser removido: "))
            if excluir_item not in Mat:
                os.system('cls')
                print(f"\n{azul}{'EXCLUSÃO DE MATERIAL':^88}{fim}\n")
                tabela()
                print(f'{amarelo}\nO código digitado não se encontra no sistema{fim}\n')
                conf = confirmação('Deseja tentar novamente?')
                if conf['opt'] == "Não":
                    return
                else:
                    os.system('cls')
                    print(f"\n{azul}{'EXCLUSÃO DE MATERIAL':^88}{fim}\n")
                    tabela()
            else:
                break
        except ValueError:
            os.system('cls')
            print(f"\n{azul}{'EXCLUSÃO DE MATERIAL':^88}{fim}\n")
            tabela()
            print(f'{amarelo}\nPor favor insira um valor válido{fim}')  

    if excluir_item in Mat:
        print('')
        conf = confirmação(f'{amarelo}Tem certeza que deseja remover?{fim}')
        if conf['opt'] == "Sim":
            del Mat[excluir_item]
            os.system('cls')
            print(f"\n{azul}{'EXCLUSÃO DE MATERIAL':^88}{fim}\n")
            tabela()
            print(f"{verde}\nMaterial removido com sucesso!\n{fim}")
        else:
            os.system('cls')
            input("Pressione ENTER para voltar ao menu")
            return             
    else:
        print("\033[31m") 
        print("Código de material não encontrado.")
    
    input("Pressione ENTER para voltar ao menu")
def reserva_de_material():
    os.system('cls')
    print(f"\n{azul}{'RESERVA DE MATERIAL':^88}{fim}\n")
    tabela()
    
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
                    tabela()
            else:
                break
        except ValueError:
            os.system('cls')
            print(f"\n{azul}{'RESERVA DE MATERIAL':^88}{fim}\n")
            tabela()
            print(f'{amarelo}\nPor favor, insira um valor válido{fim}')

    if cod_material in Mat:
        quantidade_disponivel = Mat[cod_material][1]
        os.system('cls')
        vazio = ''
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

def pesquisar():
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
    if opt['opt']=="Pesquisar por código":
        os.system('cls')
        print(f"\n{azul}{'PESQUISAR ITENS':^88}{fim}\n")
        preencher_row('', '', '', '', azul)
        chaves = ", ".join(str(key) for key in Mat.keys())
        print(f'{azul}Os códigos presentes no sistema são: {fim}{chaves}')
        while True:
            try:
                cod= int(input("\nInsira o codigo do material a ser removido: "))
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
    elif opt['opt']=="Pesquisar por nome":
        valid = False
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
                break
            else: valid = True
        if valid:
            os.system('cls')    
            print(f"\n{azul}{'PESQUISAR ITENS':^88}{fim}\n")
            preencher_row('', '' ,'' ,'', azul)
            print(f"{amarelo}Material não encontrado\n{fim}")   
        input('Pressione ENTER para voltar ao menu')
    elif opt['opt']=="Mostrar tabela":
        os.system('cls')
        print(f"\n{azul}{'PESQUISAR ITENS':^88}{fim}\n")
        tabela()
        input('\nPressione ENTER para voltar ao menu')
   
def editar():
    os.system('cls')
    print(f"\n{azul}{'EDIÇÃO DE ITENS':^88}{fim}\n")
    tabela()
    while True:
        try:
            cod= int(input("\nInsira o codigo do material a ser editado: "))
            if cod not in Mat:
                os.system('cls')
                print(f"\n{azul}{'EDIÇÃO DE ITENS':^88}{fim}\n")
                tabela()
                print(f'{amarelo}\nO código digitado não se encontra no sistema{fim}\n')
                conf = confirmação('Deseja tentar novamente?')
                if conf['opt'] == "Não":
                    return
                else:
                    os.system('cls')
                    print(f"\n{azul}{'EDIÇÃO DE ITENS':^88}{fim}\n")
                    tabela()
            else:
                break
        except ValueError:
            os.system('cls')
            print(f"\n{azul}{'EDIÇÃO DE ITENS':^88}{fim}\n")
            tabela()
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
        vazio = ''  
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
    Mat[cod][0]= nome
    Mat[cod][1]= quant
    Mat[cod][2]= valor
    print(f"{azul}\n{'Item alterado com sucesso':^88}{fim}")
    input('\nPressione ENTER para voltar para o MENU')
            

while True:
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
   