import json
import random

while True:
    print('\n--- GESTÃO FINANCEIRA ---')
    print('1. Ver quantidade de matriculados e faturamento')
    print('2. Ver pagamentos pendentes')
    print('3. Sortear Bolsa (Isentar pagamento)')
    print('4. Registrar Pagamento (Dar baixa)')
    print('5. Sair')
    acao = int(input('O que você deseja? '))

    if acao == 1:
        try:
            with open('dados_alunos.json', 'r') as arquivo:
                lista_alunos = json.load(arquivo)
        except FileNotFoundError:
            lista_alunos = []
            print("Nenhum arquivo de dados encontrado.")
            
        faturamento_total = 0

        for aluno in lista_alunos:
            if aluno.get('Pagamento') != 'Bolsista':
                if 6 <= aluno['Idade'] <= 10:
                    faturamento_total += 700 # 1 ao 5 ano
                elif 11 <= aluno['Idade'] <= 14:
                    faturamento_total += 800  # 6 ao 9 ano
                elif 15 <= aluno['Idade'] <= 17:
                    faturamento_total += 900 # 1 à 3 série
                
        print(f'\nTemos {len(lista_alunos)} alunos matriculados no momento.')
        print(f'O faturamento total previsto é de: R$ {faturamento_total},00') 

    elif acao == 2:
        try:
            with open('dados_alunos.json', 'r') as arquivo:
                lista_alunos = json.load(arquivo)
            
            print('\n--- LISTA DE PAGAMENTOS PENDENTES ---')
            encontrou_pendente = False
            
            for aluno in lista_alunos:
                if aluno.get('Pagamento') == 'Pendente':
                    valor_devido = 0
                    if 6 <= aluno['Idade'] <= 10:
                        valor_devido = 700
                    elif 11 <= aluno['Idade'] <= 14:
                        valor_devido = 800
                    elif 15 <= aluno['Idade'] <= 17:
                        valor_devido = 900
                    print(f"ID: {aluno['ID']} | Nome: {aluno['Nome']} | Idade: {aluno['Idade']} | Valor a pagar: R$ {valor_devido},00")
                    encontrou_pendente = True
            
            if not encontrou_pendente:
                print("Nenhum aluno possui pagamentos pendentes no momento.")
                
        except FileNotFoundError:
            print("Erro: O arquivo 'dados_alunos.json' não foi encontrado.")

    elif acao == 3:
        try:
            with open('dados_alunos.json', 'r') as arquivo:
                lista_alunos = json.load(arquivo)
            ids_disponiveis = [a['ID'] for a in lista_alunos if a.get('Pagamento') != 'Bolsista']
            
            if len(ids_disponiveis) == 0:
                print("Não há alunos disponíveis para sortear bolsas.")
            else:
                sorteado_id = random.choice(ids_disponiveis)

                for aluno in lista_alunos:
                    if aluno['ID'] == sorteado_id:
                        print(f'\n🎉 O aluno {aluno["Nome"]} (ID: {aluno["ID"]}) ganhou uma bolsa!')
                        aluno['Pagamento'] = 'Bolsista'
                        break
                with open('dados_alunos.json', 'w') as arquivo:
                    json.dump(lista_alunos, arquivo, indent=4)
                    
        except FileNotFoundError:
            print("Matricule alunos primeiro!")

    elif acao == 4:
        try:
            with open('dados_alunos.json', 'r') as arquivo:
                lista_alunos = json.load(arquivo)
                
            print('\n--- REGISTRAR PAGAMENTO ---')
            id_pagamento = int(input('Digite o ID do aluno que realizou o pagamento: '))
            
            aluno_encontrado = False
            for aluno in lista_alunos:
                if aluno['ID'] == id_pagamento:
                    aluno_encontrado = True
                    
                    if aluno.get('Pagamento') == 'Pago':
                        print(f"Atenção: O aluno {aluno['Nome']} já estava com o pagamento em dia!")
                    elif aluno.get('Pagamento') == 'Bolsista':
                        print(f"Atenção: O aluno {aluno['Nome']} é bolsista e é isento de pagamento!")
                    else:
                        aluno['Pagamento'] = 'Pago'
                        print(f"Sucesso! Pagamento do aluno {aluno['Nome']} foi registrado.")
                        with open('dados_alunos.json', 'w') as arquivo:
                            json.dump(lista_alunos, arquivo, indent=4)
                    break

            if not aluno_encontrado:
                print("ID não encontrado no sistema.")
                
        except FileNotFoundError:
            print("Matricule alunos primeiro!")

    elif acao == 5:
        break