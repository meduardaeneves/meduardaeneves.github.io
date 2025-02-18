"""
Regras BLACK_JACK
- O dealer vai entregar 2 cartas para você, 2 para o computador
- Você vai saber quais são suas duas cartas mas só vai saber 1 do computador
- o objetivo é ter a soma mais próxima de 21 sem ultrapassar:
    J = 10
    Q = 10
    K = 10
- você vai ter duas cartas, você pode escolher puxar uma terceira, correndo o risco de passar de 21, ou continuar com as duas que você está
- Você pode ganhar tendo 21 pontos se o valor da mão do dealer ultrapassar 21. Entretando, se sua mão tiver 22 ou mais, você perde de qualquer forma.
- VALOR DO As:
    - As pode valer 1 ou 11, você escolhe
- O computador vai continuar puxando até que a soma dele seja igual ou superior a 17
"""

blackjack_intro = """
*********************************************** LET'S PLAY BLACKJACK ***********************************************
"""

rules = """
****************************************************** REGRAS ******************************************************
- O dealer vai entregar 2 cartas para você, 2 para o computador
- Você vai saber quais são suas duas cartas mas só vai saber 1 do computador
- o objetivo é ter a soma mais próxima de 21 (ou igual a) sem ultrapassar este valor
- Cada carta tem o seu valor numérico. As demais cartas, que são letras, tem os seguinte valores:
    - A = 1 ou 11, a depender do somatório final, sempre evitando passar de 21
    - J = 10
    - Q = 10
    - K = 10
- De posse de suas duas cartas e sabendo a carta do dealer, você pode escolher puxar, ou não, uma terceira carta
    - puxando essa terceira você corre o risco de ultrapassar 21 e perder o jogo
- Você ganha o jogo nas seguintes situações:
    - Caso a soma das suas duas primeiras cartas seja 21 você ganha com blackjack
    - Caso a diferença da soma de suas cartas para 21 seja menor que a diferença da soma das cartas do dealer para 21
- Você perde o jogo:
    - Caso a soma das suas cartas ultrapasse 21
    - Caso a diferença da soma de suas cartas para 21 seja maior que a diferença da soma das cartas do dealer para 21
*********************************************************************************************************************
"""
