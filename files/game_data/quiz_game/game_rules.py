rules = """
This Game collect its data from the Open Trivia DataBase: https://opentdb.com/
- Rules:
    - The questions in this trivia game will vary in 3 aspects:
         - It's category
         - It's dificulty
         - The type of the question 
            - True of False (boolean)
            - Multiple Choice (multiple)
            - Any (both multiple and boolean)
    - You will be able to chose each one of those aspects
    - Each game consists of a maximum of 5 phases, with one question per phase.
    - You have 3 lives. If you get a question wrong, you remain in the same phase but lose a life.
    - Depending on the aspects you have chosen the game can have less than 5 phases due to the reduce amount of questions avaliable. In this case, your amount of life you be reduced to 1.
    - Your goal is to answer questions correctly and progress through the phases.
        - You earn 2 points for each phase you win.
        - You lose 1 point for each phase you fail.
        - If you reach the last phase and answer correctly, you win the game. 
        - If you run out of lives, you lose the game. 
    - If you get one question worng your game will end.
    - Once the game has ended, two parameters will be presented to you:
        - Your actual phase
        - Your total of points 
"""