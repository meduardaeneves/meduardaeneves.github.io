from sec014_mine_final_project_game_organizing_data import pop_brasil_e_ufs, pop_estados, pop_municipios
from sec014_mine_final_project_game_rules import rules
import random
import os

def escolha_municipio(municipios_ja_selecionados):
    """Vai retornar um dicionário com as informações do município que foi selecionado aleatoriamente, do seu estado e da sua região"""   
    municipio_information = {}
    
    municipio_escolhido_valido = False           
    while not municipio_escolhido_valido:
        municipio_escolhido = random.choice(list(pop_municipios.keys()))
        if municipio_escolhido not in list(municipios_ja_selecionados):  
            municipio_escolhido_valido = True
            municipios_ja_selecionados.add(municipio_escolhido)
           
    municipio_information['População Município'] = pop_municipios[municipio_escolhido]['População']
    municipio_information['Área Municipal (Km²)'] = pop_municipios[municipio_escolhido]['Área Municipal (Km²)']
    municipio_information['Sigla UF'] = pop_municipios[municipio_escolhido]['Sigla UF']
    municipio_information['Município'] = municipio_escolhido.split(' - ')[0]
    municipio_information['Nome UF'] = pop_estados[municipio_information['Sigla UF']]['Nome UF']
    municipio_information['População UF'] = pop_estados[municipio_information['Sigla UF']]['População']
    municipio_information['Região'] = pop_estados[municipio_information['Sigla UF']]['Região Pertencente']
    municipio_information['População Região'] = pop_brasil_e_ufs[municipio_information['Região']]
    
    return municipio_information, municipios_ja_selecionados 

def pontuacao_rodada(qnt_dicas):
    if qnt_dicas == 0:
        pontuacao = 3
    elif qnt_dicas == 1:
        pontuacao = 2
    else:
        pontuacao = 1
    return pontuacao

def imprimir_informacoes_cidade(loop,cidade,dica):
    informacao_estado = f' - Estado: {cidade['Nome UF']} ({cidade['Sigla UF']})'
    if loop == 0:
        pop_cidade = f' - População da cidade: {cidade['População Município']:,.0f} hab'
    else:
        pop_cidade = ''
    informacao_cidade = f'{loop+1} Cidade: "{cidade['Município']}"{pop_cidade}' 
    if dica != 0:
        informacao_estado += f'- População do Estado: {cidade['População UF']:,.0f} hab.'
        if dica == 2:
            informacao_cidade += f'\n   - Extensão Territorial de "{cidade['Município']}": {cidade['Área Municipal (Km²)']:,.0f} Km²'    
    print(f'{informacao_cidade}\n{informacao_estado}\n - Região: {cidade['Região']} - População da Região: {cidade['População Região']:,.0f} hab.\n')

def receber_dica(ordem_dica,qnt_jogos_corretos,qnt_pontuacao,municipios,qnt_dicas):
    dica = input(f'Você gostaria de pegar a {ordem_dica+1}a dica? [S] para sim ou qualquer outra coisa para não: ').upper()
    if dica == 'S' or dica == 'SIM':
        qnt_dicas += 1
        os.system('cls')
        print('ESTAMOS JOGANDO "HIGER OR LOWER"\n')
        if qnt_jogos_corretos == 0:
            print(rules)
        else:
            print(f' - Pontuação Atual: {qnt_pontuacao}; Jogos Corretos: {qnt_jogos_corretos}\n')
        for i,municipio in enumerate(municipios):
            imprimir_informacoes_cidade(i,municipio,qnt_dicas)
    return qnt_dicas

def receber_resposta_usuario(municipios,opcoes_jogo):
    verify_guess = False
    print(f'\nVocê acha que "{municipios[1]['Município']}" tem mais ou menos habitantes que "{municipios[0]['Município']}"?')
    while not verify_guess:
        acerto = input(f'Digite [MAIS] para MAIS ou [MENOS] para MENOS: ').upper()
        if acerto not in opcoes_jogo:
            print('Você escreveu uma resposta não válida.')
        else:
            verify_guess = True
    return acerto

def verificar_vitoria(aposta_final,municipios,jogos_corretos,pontuacao,qnt_dicas):
    perde_ganhou = False
    if aposta_final == 'MAIS':
        if municipios[1]['População Município'] >= municipios[0]['População Município']:
            jogos_corretos += 1
            pontuacao += pontuacao_rodada(qnt_dicas)
            perde_ganhou = True
        else:
            perde_ganhou = False   
    else:
        if municipios[1]['População Município'] < municipios[0]['População Município']:
            jogos_corretos += 1
            pontuacao += pontuacao_rodada(qnt_dicas)
            perde_ganhou = True
        else:
            perde_ganhou = False

    print()
    print('COMPARANDO AS POPULAÇÕES:')
    print(f' - {municipios[0]['Município']}: {municipios[0]['População Município']:,.0f} habitantes; {municipios[1]['Município']}: {municipios[1]['População Município']:,.0f} habitantes\n') 
    if perde_ganhou == True:
        print('VOCÊ GANHOU ESSA FASE E VAI AVANÇAR PARA A PRÓXIMA.')
    else:
        print('VOCÊ PERDEU O JOGO.')     
    return perde_ganhou,jogos_corretos, pontuacao


##JOGO COMEÇA AQUI

def play_high_or_low():
    municipios_selecionados = set()
    opcoes_jogo = ['MAIS','MENOS']
    qnt_jogos_corretos = 0
    qnt_pontuacao = 0
    prox_fase = True
    
    while prox_fase:
        qnt_dicas = 0
        print('ESTAMOS JOGANDO "HIGER OR LOWER"\n')
        if qnt_jogos_corretos == 0:
            print(rules)
            municipios_em_jogo = []
            for i in range(2):
                municipios, municipios_selecionados = escolha_municipio(municipios_selecionados)
                municipios_em_jogo.append(municipios)
                imprimir_informacoes_cidade(i,municipios,qnt_dicas)
        else:
            print(f' - Pontuação Atual: {qnt_pontuacao}; Jogos Corretos: {qnt_jogos_corretos}\n')
            del municipios_em_jogo[0]
            municipio, municipios_selecionados = escolha_municipio(municipios_selecionados)
            municipios_em_jogo.append(municipio)
            for i in range(2):
                imprimir_informacoes_cidade(i,municipios_em_jogo[i],qnt_dicas)     
                   
        for i in range(2):
            if i == 0:
                qnt_dicas = receber_dica(i,qnt_jogos_corretos,qnt_pontuacao,municipios_em_jogo,qnt_dicas)        
            if i == 1 and qnt_dicas == 1:
                qnt_dicas = receber_dica(i,qnt_jogos_corretos,qnt_pontuacao,municipios_em_jogo,qnt_dicas)
            
        guess = receber_resposta_usuario(municipios_em_jogo,opcoes_jogo)

        prox_fase,qnt_jogos_corretos,qnt_pontuacao = verificar_vitoria(guess,municipios_em_jogo,qnt_jogos_corretos,qnt_pontuacao,qnt_dicas)
        print(f' - Pontuação Total: {qnt_pontuacao}; Jogos Corretos: {qnt_jogos_corretos}') 
        if prox_fase:
            continuar_prof_fase = input('Aperte qualquer tecla para ir à proxima fase.')
            if isinstance(continuar_prof_fase,str):
                os.system('cls')

    play_again = input('\nVocê quer jogar novamente? [S] para sim ou qualquer outra coisa para não: ').upper()
    if play_again == 'S' or play_again == 'SIM':
        os.system('cls')
        play_high_or_low()
    else:
        return

play_high_or_low()    
    
    
    
    
