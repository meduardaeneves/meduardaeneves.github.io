---
layout: archive
title: "CV"
permalink: /cv_pt/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

<p>Sou Desenvolvedora Jr. em transição de carreira, com sólida base analítica adquirida na graduação em Engenharia Civil. Atualmente, curso especialização em Deep Learning pelo CIN‑UFPE, onde aprofundomeus conhecimentos em inteligência artificial e programação. Tenho experiência prática no desenvolvimento de projetos com Python, incluindo a integração com APIs para coleta e tratamento de dados externos. Além disso, realizei cursos complementares que me proporcionaram conhecimentos básicos em JavaScript, HTML, CSS e SQL, ampliando minha atuação no desenvolvimento web e na análise de dados.</p>

<p>Para acessar a versão em inglês desta página <a href='https://meduardaeneves.github.io//cv/'>Clique aqui</a>.</p>
<p>É possível baixar o PDF do currículo em duas línguas: <a href='https://raw.githubusercontent.com/meduardaeneves/meduardaeneves.github.io/master/files/cv_models/CV_Maria_Eduarda_ESTEVES_NEVES.pdf'>PORTUGUÊS</a> e <a href='https://raw.githubusercontent.com/meduardaeneves/meduardaeneves.github.io/master/files/cv_models/CV_Maria_Eduarda_ESTEVES_NEVES_en.pdf'>INGLÊS</a>. Clique na lingua que deseja baixar.</p>

Formação Acadêmica
======
**Pós-Graduação Lato Sensu (Especialização) em Deep Learning, Recife - PE - Brasil** 
* CIN - UFPE, novembro 2023 – atual

**MBA em Infraestrutura de Transporte, Minas Gerais - BH - Brasil**
* PUC - Minas, setembro 2022 – dezembro 2023

**Graduação em Engenharia Civil, Recife – PE - Brasil**
* UFPE, março 2016 – junho 2022
  * Média Geral: 8.32 / 10.00

**Graduação sanduíche em Engenharia Civil, Lille - France**
* Polytech Lille, setembro 2018 – junho 2019
  * Quarto ano do bacharelado de engenharia civil na Universidade Polytech Lille.
  * Bolsista de excelência através do programa BRAFITEC, Capes.

Habilidades
======
* **Banco de Dados:** SQL Básico;
* **Deep Learning:** Machine Learning; Visão Computacional
* **Front‑End (Noção Básica):** JavaScript; HTML; CSS
* **Linguagem Back‑end:** Python e bibliotecas relacionadas (Pandas; Plotly)
* **Microsoft Office Avançado:** Excel, Power Point; Word
* **Raciocínio Lógico:**
* **Softwares de Engenharia:** AutoCAD; AutoCAD Civil 3D; QGIS
* **Versionamento e colaboração de código:** Git e GitHub


Experiência Profissional
======
**Assistente de Engenharia Civil, Recife - PE - Brasil** 
* TPF Engenharia, agosto 2022 – agosto 2023
  * Utilização de softwares como Civil 3D e Excel para desenvolvimento de projeto de drenagem em infraestrutura.
  * Concepção do projeto e dimensionamento dos dispositivos de drenagem a serem utilizados.

**Auxiliar de Engenharia Civil, Recife - PE - Brasil** 
* TPF Engenharia, setembro 2021 – agosto 2022
  * Assistente na fase final do estudo de viabilidade de uma nova ferrovia;
  * Utilização de softwares como Civil 3D e QGIS para desenvolvimento de projeto de drenagem em infraestrutura.

**Monitoria Universitária, Recife - PE - Brasil** 
* UFPE, agosto 2020 – abril 2021
  * Monitoria da disciplina de Geometria Gráfica Tridimensional;
  * Períodos universitários: 2020.3 e 2020.1.

**Estagiária de Engenharia Civil, Recife - PE - Brasil** 
* TPF Engenharia, setembro 2019 – setembro 2021
  * **Equipe de Infraestrutura**
    * Auxiliar no desenvolvimento de um estudo de viabilidade para uma nova ferrovia a ser implantada no Brasil.
  * **Equipe de Cartografia**
    * Auxiliar em um projeto de regularização fundiária;
    * Utilização do Qgis para mapeamento de informações e edição de dados georreferenciados;
    * Desenvolvimento atlas e de mapas cartográficos.
  * **Equipe de Qualidade**
    * Desenvolvimento de pesquisas sobre realidade virtual e realidade aumentada.

**Estagiária de Engenharia Civil, Recife - PE - Brasil** 
* Melo Gouveia Construção e Incorporação, agosto 2017 – agosto 2018
  * Monitoramento da construção de um imóvel residencial.
  * Gerenciamento de pessoas e material da construção civil.
  
Cursos e Certificados
======
* Algoritmo ; Por: Curso em Vídeo ; Certificado No. B3BC8-6297-9;  
* AutoCAD módulo 1 (Essential) ; Por: StudioCAD ; Certificado No. 1PNFTTBF4;  
* Curso Completo: SQL para Análise de Dados com BigQuery ; Por: Udemy; 
* Jornada Python ; Por: Hashtag; 
* Machine Learning: Clusterização com linguagem Python ; Por: Udemy; 
* Microsoft Excel 2016 Avançado ; Por: Fundação Bradesco ; Certificado No. DCE9877D-34D8-4CEF-84E1-562F388CC7E0;  
* Project101x: Introdução ao gerenciamento de projetos ; Por: AdelaideX ; Certificado No. 5f52fa5a98114052a891645a59b49615;
* Orientação a Objetos com JavaScript (Projetos e TypeScript);
* Trabalhando em equipes ágeis ; Por: DIO ; Certificado No. 3A5A21A4  

Línguas
======
* Português: Nativo
* Inglês: Fluente – ECPE C2 (Credenciais 336100006)
* Francês: Intermediário 
  
Reconhecimento e Prêmios
======
* Bolsa de Estudo BRAFITEC para alunos de Excelência fornecida pela CAPES: Graduação sanduíche na França.

Publicações
======
<!--
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
-->
  <ul>
    {% assign allowed_categories = "livros,manuscritos,congressos" | split: "," %}
    {% for post in site.publications reversed %}
      {% if allowed_categories contains post.category and post.language == "port" %}
        {% include archive-single-cv.html %}
      {% endif %}
    {% endfor %}
  </ul>


<!--
Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Service and leadership
======
* Currently signed in to 43 different slack teams
-->
