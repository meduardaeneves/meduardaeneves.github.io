# Plotly & Pandas: Movie Data Visual Analysis
# Links de acesso:
- [Link para acesso ao Google Colab](https://colab.research.google.com/drive/12QTalEdwHfajrw17FiNzaJlCpPPo2y90?usp=sharing)
- Arquivo ".ipynb" para rodar o projeto: plotly_pandas_movies_visual_analysis.ipynb
- [Link de acesso para o portfólio em Inglês](https://meduardaeneves.github.io/portfolio/personal-projects/plotly_pandas_movies_visual_analysis/)

# Objetivos do Projeto

- O projeto tem como objetivo aplicar uma análise descritiva de um "Movie Lens Data"
- Os dados foram coletados por meio do ["Group Lens"](http://files.grouplens.org/datasets/movielens/), através de seus arquivos "movielens" "ml-100k/".
- Os arquivos utilizados durante o projeto foram: u.data; u.item e u.user
- Este Projeto foi desenvolvido durante o curso de Pós-graduação em Deep Learning e como formato de Pergunta e Resposta. Portanto, o projeto foi organizado de forma a responder às questões que foram feitas, utilizando as bibliotecas python PLOTLY e PANDAS.
- Por fim, este projeto teve como objetivo principal desenvolver conhecimento nas bibliotecas PANDAS e PLOTLY

# Desenvolvimento do Projeto

O desenvolvimento técnico deste projeto foi dividido em Carregamento dos Dados, seguido por suas 2 fases (2 questões principais)
1. Apresentação em formato visual (usando Plotly) dos arquivos de Minessota
2. Manipulação de DataFrame usando Pandas

## Carregamento dos Dados

## Apresentação em formato visual (usando Plotly) dos arquivos de Minessota

## Manipulação de DataFrame usando Pandas
- Esta fase final focou em manipular os DataFrames trabalhando com os elementos da biblioteca Pandas
- A primeira manipulação feita foi a geração de um novo DataFrame com apenas usuários "Masculino" (M) e "Estudante" (student), maiores de 20 anos.
  - Uma função foi aplicada no conjunto de dados USER:
    -   student_users = users[(users.age > 20)&(users.occupation == "student")&(users.gender == "M")]
  - A tabela abaixo apresenta um fragmento do novo DataFrame que foi gerado
- A segunda manipulação foi feita para descobrir a quantidade de mulheres programadoras que existem
  - Uma função foi aplicada no conjunto de dados USER:
    - programmer_F_users = users[(users.occupation == "programmer")&(users.gender == "F")]
  -  Foi encontrado um total de 6 usuários que se encaixam nos critérios
- A última manipulação foi feita para descobrir a quantidade de filmes com classificação acima de 3
  - Uma função foi aplicada no conjunto de dados DATA:
    - over3_data = data[data.rating > 3]
  - Resultados por classificação (4 e 5): Classificação 4 com 34.174 unidades; Classificação 5 com 21.201 unidades
  - Foram encontrados 55.375 filmes com avaliações acima de 3
