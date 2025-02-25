"""The data used was extracted from IBGE: 
- População: https://www.ibge.gov.br/estatisticas/sociais/populacao/9103-estimativas-de-populacao.html
- Área Territorial: https://www.ibge.gov.br/geociencias/organizacao-do-territorio/estrutura-territorial/15761-areas-dos-municipios.html
"""
import os
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).parent
DATA_PATH_POP = ROOT / 'estimativa_dou_2024.xlsx'
DATA_PATH_AREA = ROOT / 'AR_BR_RG_UF_RGINT_MES_MIC_MUN_2022.xlsx'

BRASIL_E_UFS = ['Brasil','Norte','Nordeste','Sudeste','Sul','Centro-Oeste']
pop_brasil_e_ufs = {}
pop_estados = {}
siglas_estados_df = {
    'Acre': 'AC',
    'Alagoas': 'AL',
    'Amapá': 'AP',
    'Amazonas': 'AM',
    'Bahia': 'BA',
    'Ceará': 'CE', 
    'Distrito Federal': 'DF',
    'Espírito Santo': 'ES',
    'Goiás': 'GO',
    'Maranhão': 'MA',
    'Mato Grosso': 'MT',
    'Mato Grosso do Sul': 'MS',
    'Minas Gerais': 'MG',
    'Pará': 'PA',
    'Paraíba': 'PB',
    'Paraná': 'PR',
    'Pernambuco': 'PE',
    'Piauí': 'PI',
    'Rio de Janeiro': 'RJ',
    'Rio Grande do Norte': 'RN',
    'Rio Grande do Sul': 'RS',
    'Rondônia': 'RO',
    'Roraima': 'RR',
    'Santa Catarina': 'SC',
    'São Paulo': 'SP',
    'Sergipe': 'SE',
    'Tocantins': 'TO',
}

def print_dict(dict):
    for element in dict:
        print(f'População {element}: {dict[element]}')

df_estados = pd.read_excel(DATA_PATH_POP,sheet_name='BRASIL E UFs',skiprows=[0],thousands='.',decimal=',')
df_estados = df_estados.drop(axis=0,index=df_estados.index[[-1,-2]])

for index, row in df_estados.iterrows():
    # print(index,row['BRASIL E UNIDADES DA FEDERAÇÃO'],row['POPULAÇÃO ESTIMADA'])
    if row['BRASIL E UNIDADES DA FEDERAÇÃO'] in BRASIL_E_UFS:
        pop_brasil_e_ufs[row['BRASIL E UNIDADES DA FEDERAÇÃO']] =  row['POPULAÇÃO ESTIMADA']
        if row['BRASIL E UNIDADES DA FEDERAÇÃO'] != 'Brasil':
           regiao_pertencente = row['BRASIL E UNIDADES DA FEDERAÇÃO'] 
    else:
        # if row['BRASIL E UNIDADES DA FEDERAÇÃO'] == 'Distrito Federal':       
        sigla = siglas_estados_df[row['BRASIL E UNIDADES DA FEDERAÇÃO']]
        pop_estados[sigla] = {
            'População': row['POPULAÇÃO ESTIMADA'], 
            'Nome UF': row['BRASIL E UNIDADES DA FEDERAÇÃO'],
            'Região Pertencente': regiao_pertencente} 
    
df_municipios = pd.read_excel(DATA_PATH_POP,sheet_name='MUNICÍPIOS',skiprows=[0],thousands='.',decimal=',')
df_municipios = df_municipios.drop(axis=0,index=df_municipios.index[[-1,-2]]) 

pop_municipios = {}
for index, row in df_municipios.iterrows():
    pop_municipios[f'{row['NOME DO MUNICÍPIO']} - {row['UF']}'] = {'População': row['POPULAÇÃO ESTIMADA'],'Sigla UF': row['UF']}


df_municipios_area = pd.read_excel(DATA_PATH_AREA,sheet_name='AR_BR_MUN_2022',thousands='.',decimal=',')
df_municipios_area = df_municipios_area.drop(axis=0,index=df_municipios_area.index[[-1,-2,-3]]) 

municipios_inexistente_tabela_pop = []
for index, row in df_municipios_area.iterrows():
    municipio_area = row['AR_MUN_2022'] 
    municipio_area_name = f'{row['NM_MUN']} - {row['NM_UF_SIGLA']}'
    try:
        pop_municipios[municipio_area_name]['Área Municipal (Km²)'] = municipio_area    
    except:
        municipios_inexistente_tabela_pop.append(municipio_area_name)

# print(len(pop_municipios))
# print_dict(pop_municipios)


        






