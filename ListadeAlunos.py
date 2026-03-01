Alunos = []
indice = 1
Qtdalunos = 0
qtdmatriculados15 = 0
qtdmatriculados13 = 0
qtdmatriculados69 = 0

import json

try:
    with open('dados_alunos.json', 'r') as arquivo:
        Alunos = json.load(arquivo)
except FileNotFoundError:
    Alunos = []

def salvar_dados():
    with open('dados_alunos.json', 'w') as arquivo:
        json.dump(Alunos, arquivo, indent=4)

try:
    with open('dados_alunos.json', 'r') as arquivo:
        Alunos = json.load(arquivo)
        if len(Alunos) > 0:
            indice = max(aluno['ID'] for aluno in Alunos) + 1
        else:
            indice = 1
except FileNotFoundError:
    Alunos = []
    indice = 1

if __name__ == '__main__':
    while True:
        print(' --- SISTEMA DE MATRICULAS ---')
        print(' --- 1. Matricular Aluno ---')
        print(' --- 2. Listar Alunos ---')
        print(' --- 3. Remover Aluno ---')
        print(' --- 4. Alunos Total ---')
        print(' --- 5. sair ---')
        acao = int(input())

        if acao == 1:
            print('Nome do aluno: ')
            nome = input()
            print(f'Idade do {nome}: ')
            idade = int(input())
        
            Novo_aluno = {'Nome': nome, 'Idade': idade, 'ID': indice, 'Pagamento': 'Pendente'}
            if Novo_aluno not in Alunos:
                Alunos.append(Novo_aluno)
                indice = indice + 1
                Qtdalunos = Qtdalunos + 1
                salvar_dados()

                if 6 <= Novo_aluno['Idade'] <= 10:
                    qtdmatriculados15 += 1
                elif 11 <= Novo_aluno['Idade'] <= 14:
                    qtdmatriculados69 += 1
                elif 15 <= Novo_aluno['Idade'] <= 17:
                    qtdmatriculados13 += 1
                print(f'O Aluno {nome} de {idade} anos, foi matriculado')
            else:
                print('aluno ja matriculado')
                continue
        elif acao == 2:
            if len(Alunos) == 0:
                print('voce nao tem nenhum aluno matriculado')
                continue
            else:
                for aluno in Alunos:
                    print(f'Nome: {aluno['Nome']} | Idade: {aluno['Idade']} | ID: {aluno['ID']}')
                print('Deseja pesquisar por um aluno?')
                acaopesquisa = input("Sim ou nao?")
                if acaopesquisa == 'sim'.lower():
                    print('Digite a letra do nome: ')
                    letradebusca = input()
                    for letra in Alunos:
                        if letra['Nome'].lower().startswith(letradebusca.lower()):
                            print(f'ALuno: {letra['Nome']}')
        elif acao == 3:
            if len(Alunos) == 0:
                print('voce nao tem nenhum aluno matriculado')
                continue
            else:
                print('digite o ID do aluno que deseja remover')
                iddesejado = int(input())
                aluno_encontrado = None
                for aluno in Alunos:
                    if aluno['ID'] == iddesejado:
                        aluno_encontrado = aluno
                        break
                if aluno_encontrado:
                    Alunos.remove(aluno_encontrado)
                    Qtdalunos = Qtdalunos - 1
                    salvar_dados()
                    print(f'o aluno: {aluno['Nome']} do ID: {aluno['ID']} foi removido ')
                else:
                    print('id nao encontrado')
        elif acao == 4:
            for aluno in Alunos:
                print(f'Nome: {aluno['Nome']} | Idade: {aluno['Idade']} | ID: {aluno['ID']}')
            print(f'Numero total de alunos: {len(Alunos)}')
        elif acao == 5:
            break

    print('=== SUA LISTA DE ALUNOS ===')
    for aluno in Alunos:
        print(f'Nome: {aluno['Nome']} | Idade: {aluno['Idade']} | ID: {aluno['ID']}')