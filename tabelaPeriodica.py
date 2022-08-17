##############################################################
#Projeto: tabela periodica                                   #
#Materia: Estrutura De Dados / 2º semestre                   #
#Aluno: Arthur Fagundes                                      #
##############################################################


import csv
import os

periodicTable = {}
states = {'l': 'Líquido', 'g': 'Gasoso', 's': 'Sólido'}
table = {}

archive = csv.reader(open('tabela.txt'), delimiter=';')
for size, line_data in enumerate(archive):
    if size == 0:
        continue

    data = {}
    data['simbolo'] = line_data[0]
    data['nome'] = line_data[1]
    data['atomico'] = line_data[2]
    data['linha'] = line_data[3]
    data['coluna'] = line_data[4]
    data['estado'] = line_data[5]

    table[size] = data
    periodicTable[data['simbolo']] = data


def answerValidation():
    if correctAnswer == True:
        showElement()
    else:
        print('Elemento Inválido.')


def elementValidation():
    if correctAnswer == True:
        dataSelect = input('Qual dado deseja exibir?\n')
        if dataSelect == 'simbolo':
            os.system('cls')
            print("Simbolo:", periodicTable[element]["simbolo"])
        elif dataSelect == 'nome':
            os.system('cls')
            print("Nome:", periodicTable[element]["nome"])
        elif dataSelect == 'atomico':
            os.system('cls')
            print("Atômico:", periodicTable[element]["atomico"])
        elif dataSelect == 'linha':
            os.system('cls')
            print("Linha:", periodicTable[element]["linha"])
        elif dataSelect == 'coluna':
            os.system('cls')
            print("Coluna:", periodicTable[element]["coluna"])
        elif dataSelect == 'estado':
            os.system('cls')
            print("Estado:", states[periodicTable[element]["estado"]])
        else:
            print('Dado selecionado é inválido.')
    else:
        ('Esse elemento não existe.')


def showElement():
    simbolo = periodicTable[element]["simbolo"]
    nome = periodicTable[element]["nome"]
    atomico = periodicTable[element]["atomico"]
    linha = periodicTable[element]["linha"]
    coluna = periodicTable[element]["coluna"]
    estado = states[periodicTable[element]["estado"]]

    print(f"""
{nome:=^40}
Simbolo: {simbolo}
Atômico: {atomico}
Linha: {linha}
Coluna: {coluna}
Estado: {estado}
{'='*40}
""")


option = int(input('''
O que você quer?
[1] Ver todos os Elementos.
[2] Buscar por um elemento e ver seus dados.
[3] Bucar com um elemento e ver um dado específico.\n'''))

if option == 1:
    os.system('cls')
    elementTable = ", ".join([str(_) for _ in periodicTable])
    elementTableList = list(elementTable.split(', '))
    for element in elementTableList:
        showElement()
elif option == 2:
    elementTable = ", ".join([str(_) for _ in periodicTable])
    elementTableList = list(elementTable.split(', '))
    element = input('Qual elemento?\n').capitalize()
    for i in elementTableList:
        if element == i:
            os.system('cls')
            correctAnswer = True
            answerValidation()
            break
        else:
            os.system('cls')
            correctAnswer = False
            answerValidation()

elif option == 3:
    elementTable = ", ".join([str(_) for _ in periodicTable])
    elementTableList = list(elementTable.split(', '))
    element = input('Qual elemento?\n').capitalize()
    for i in elementTableList:
        if element == i:
            correctAnswer = True
            os.system('cls')
            elementValidation()
            break
        else:
            correctAnswer = False
            os.system('cls')
            elementValidation()
else:
    print('Essa opção não é válida...')
