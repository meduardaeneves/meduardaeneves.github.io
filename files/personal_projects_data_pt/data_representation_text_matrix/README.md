# Data Representation: Text Transformation to Matrix
# Links de acesso:
- [Link para acesso ao Google Colab](https://colab.research.google.com/drive/1_dzpF8m8Em1LeV0zFrEsZfcaB_zju_Rg?usp=sharing)
- Arquivo ".ipynb" para rodar o projeto: data_representation_text_matrix.ipynb
- [Link de acesso para o portfólio em Inglês](https://meduardaeneves.github.io/portfolio/personal-projects/data_representation_text_matrix/)

# Objetivos do Projeto
- O projeto tem como objetivo desenvolver uma matriz numérica a partir de um texto em txt . 
- Após o desenvolvimento da matriz, o projeto também a converte de volta para o formato do texto original

# Desenvolvimento do Projeto
- Para solucionar o problema em questão, este projeto optou por fragmentar o desenvolvimento técnico em três partes:
- Carregamento dos dados
- Conversão do texto para matriz numérica
- Conversão da matriz numérica para texto

## Carregamento dos Dados
- O texto .txt foi fornecido durante o curso de Pós-graduação e pode ser visto no repositório do projeto.
- Abaixo é possível ler suas frases iniciais:

"De motu Circulari Fluidorum.

 Hypothesis.

 Resistentiam, quæ oritur ex defectu lubricitatis partium Fluidi, cæteris paribus, proportionalem esse 
 velocitati, qua partes Fluidi separantur ab invicem."

## Conversão do texto para matriz numérica
- A ideia é converter o texto em matriz onde sua quantidade de linhas e colunas depende da estrutura do texto.
 - Cada linha no texto é uma linha na matriz
 - A quantidade de colunas foi definida pela linha que tem a maior quantidade de palavras.
 - As linhas que tinham menos palavras, foram completadas com o texto "None", quantas vezes fosse necessário, até que tivesse a mesma quantidade de palavras da frase mais longa.
 - Depois disso, havia uma matriz de texto, mas ainda com palavras e não números
- Cada palavra apresentada no vocabulário do texto recebeu um valor numérico, criando uma "matriz de conversão"
- Na posse do elemento de conversão e da matriz de texto, foi possível criar uma nova matriz numérica, que representava o texto
- Abaixo está uma representação da matriz e algumas informações sobre os números usados para converter o texto e as palavras relacionadas a ele:
 - Total de palavras encontradas no texto: 3303
 - Vocabulário total encontrado no texto: 1322
 - Exemplo de texto - conversão de número:

[..., (3, 'quiescentibus,'), (4, 'motus'), ...,(297, 'Circulari'),..., (434, 'motu'),..., (1125, 'De'),...]

- Representação da matriz numérica criada:

<p>[[1125 &nbsp;&nbsp;434 &nbsp;&nbsp;297 ... 1322 1322 1322]<br>
&nbsp;[1169 1322 1322 ... 1322 1322 1322]<br>
&nbsp;[&nbsp;&nbsp;861 1322 1322 ... 1322 1322 1322]<br>
&nbsp;...<br>
&nbsp;[1040 1322 1322 ... 1322 1322 1322]<br>
&nbsp;[&nbsp;&nbsp;&nbsp;&nbsp;25 &nbsp;&nbsp;763 &nbsp;&nbsp;231 ... 1187 &nbsp;&nbsp;541 1171]<br>
&nbsp;[&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 1322 1322 ... 1322 1322 1322]]</p>

## Conversão da matriz numérica para texto 
- O processo para converter a matriz numérica no texto original é o inverso do apresentado no último tópico
- O "conversor texto-número" é usado para transformar os valores numéricos da matriz em palavras
- Depois disso, uma matriz de texto é obtida juntando os elementos na mesma linha, adicionando espaços
- Uma vez que cada linha nesta matriz é uma linha do texto, a conversão final é feita, juntando todas as linhas.
- A fração do resultado final é apresentada abaixo. Observa-se que é igual ao texto demonstrado no início do projeto.

"De motu Circulari Fluidorum.

 Hypothesis.

 Resistentiam, quæ oritur ex defectu lubricitatis partium Fluidi, cæteris paribus, proportionalem esse 
 velocitati, qua partes Fluidi separantur ab invicem."

