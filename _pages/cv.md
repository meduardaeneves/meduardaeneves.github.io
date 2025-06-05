---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

<p>I am a Junior Developer transitioning from a career in Civil Engineering, where I built a strong analytical foundation. I am currently pursuing a specialization in Deep Learning at CIN‑UFPE, deepening my knowledge in artificial intelligence and programming. I have hands‑on experience developing projects with Python, including integrating external APIs for data collection and processing. Additionally, I have completed courses that provided me with knowledge of JavaScript, HTML, CSS, and SQL, expanding my capabilities in web development and data analysis.</p>

<p>To access the portuguese version of this page <a href='https://meduardaeneves.github.io//cv_pt/'>Click Here</a>.</p>
<p>It is possible to download the CV's PDF format in two languages: <a href='https://raw.githubusercontent.com/meduardaeneves/meduardaeneves.github.io/master/files/cv_models/CV_Maria_Eduarda_ESTEVES_NEVES.pdf'>PORTUGUESE</a> and <a href='https://raw.githubusercontent.com/meduardaeneves/meduardaeneves.github.io/master/files/cv_models/CV_Maria_Eduarda_ESTEVES_NEVES_en.pdf'>ENGLISH</a>. Click on the language you want to download.</p>

Education
======
**Postgraduate, specialization in Deep Learning, Recife - PE - Brazil** 
* CIN - UFPE, November 2023 - Current

**Postgraduate, specialization in Transportation and Infrastructure, Minas Gerais - BH - Brazil**
* PUC - Minas, September 2022 - December 2023

**B.S. in Civil Engineering, Recife - PE - Brazil**
* UFPE, March 2016 - June 2022
  * GPA: 8.32 / 10.00

**B.S. exchange program in Civil Engineering, Lille - France**
* Polytech Lille, September 2018 - June 2019
  * Fourth year of the Civil Engineering B.S. program
  * BRAFITEC excellence scholarship granted by a Brazilian corporation called CAPES.

Skills
======
* **Database Management:** Basic SQL;
* **Deep Learning:** Machine Learning; Computer Vision
* **Front‑End (Basic Knowledge):** JavaScript; HTML; CSS
* **Back‑end Languages:** Python and Libraries (Pandas; Plotly)
* **Advanced Microsoft Office:** Excel, Power Point; Word
* **Logical Thinking:**
* **Engineering Software:** AutoCAD; AutoCAD Civil 3D; QGIS
* **Versioning and Code Collaboration:** Git and GitHub

Work experience
======
**Civil Engineering Assistant, Recife - PE - Brazil** 
* TPF Engenharia, August 2022 - August 2023
  * Usage of softwares such as Civil 3D and Excel to develop infrastructure drainage projects;
  * Project conception and dimensioning of drainage equipment devices

**Civil Engineering Assistant, Recife - PE - Brazil** 
* TPF Engenharia, September 2021 - August 2022
  * Assistant in the final phase of a feasibility study for a new railway to be deployed;
  * Use of Civil 3D and QGIS softwares to develop a drainage system for infrastructure projects.

**Teacher Assistant Internship, Recife - PE - Brazil** 
* UFPE, August 2020 - April 2021
  * Teaching assistant of Tridimensional Graphic Geometry course;
  * University’s period: 2020.3 and 2020.1.

**Civil Engineering Intern, Recife - PE - Brazil** 
* TPF Engenharia, September 2019 - September 2021
  * **Infrastructure Team**
    * Assist in the development of a feasibility study for a new railway to be deployed in Brazil.
  * **Cartography Team**
    * Assist in a land regularization project;
    * Use of QGIS software for mapping features and data editing;
    * Development and creation of maps.
  * **Quality Management Team**
    * Research of virtual and augmented reality to be implanted in the company´s future.

**Civil Engineering Intern, Recife - PE - Brazil** 
* Melo Gouveia Construção e Incorporação, August 2017 - January 2018
  * Surveillance for a residential building construction
  * Construction Management

  
Courses and Certificates
======
* Algorithm ; BY: Curso em Vídeo ; Certificate No. B3BC8-6297-9;  
* AutoCAD module 1 (Essential)  ; BY: StudioCAD ; Certificate No. 1PNFTTBF4;  
* Complete Course: SQL for Data Analisys with BigQuery ; BY: Udemy; 
* Python Journey ; BY: Hashtag; 
* Machine Learning: Clusterization with Python  ; BY: Udemy; 
* Advanced 2016 Microsoft Excel ; BY: Fundação Bradesco ; Certificate No. DCE9877D-34D8-4CEF-84E1-562F388CC7E0;  
* Project101x: Introduction to Project Management ; BY: AdelaideX ; Certificate No. 5f52fa5a98114052a891645a59b49615;
* Object‑Oriented Programming with JavaScript (Projects and TypeScript)  ; BY: Udemy; 
* Working on agile teams ; BY: DIO ; Certificate No. 3A5A21A4  
  
Languages
======
* Portuguese: Native
* English: Fluent – ECPE C2 (Credential 336100006)
* French: Intermediate 
  
Honors and Awards
======
* Academic Excellence Exchange Scholarship – Brafitec 2018

Publications
======
<!--
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
-->
  <ul>
  {% assign allowed_categories = "books,manuscripts,conferences" | split: "," %}
  {% for post in site.publications reversed %}
    {% if allowed_categories contains post.category %}
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
