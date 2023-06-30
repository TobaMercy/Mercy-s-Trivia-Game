game = ("WELCOME TO MERCY'S SPACE TRIVIA GAME")
print(game)

def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("--------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, or C): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    
    display_score(correct_guesses, guesses)

# --------------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# --------------------------------
def display_score(correct_guesses, guesses):
    print("--------------------------------")
    print("RESULTS")
    print("--------------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end="")
        print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end="")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("YOUR SCORE IS: "+str(score)+"%")


# --------------------------------
def play_again():
    
    response = input("Do you want to play again?: (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

# --------------------------------


questions = {
    "What is the natural satellite of the earth?: ": "C",
    "What is the process by which a star releases energy?: ": "B",
    "What is the smallest planet in the solar system?: ": "A",
    "What is the process of a star exploding at the end of its life  called?: ": "A",
    "What is the term for a small rocky object that orbits the Sun?: ": "C",
    "What is the largest planet in our solar system?: ": "B",
    "What is the name of the galaxy that contains our solar system?: ": "B",
    "What is the outermost layer of the Sun called?: ": "A",
    "What is the force that keeps planets in orbit around the Sun called?: ": "C",
    "What is the name of the first artificial satellite launched?: ": "B"
}


options = [["A. Sun", "B. Star", "C. Moon"], 
           ["A. Gravity", "B. Fusion", "C. Work"],
           ["A. Mercury", "B. Saturn", "C. Pluto"],
           ["A. Supernova", "B. Fusion", "C. Gravity"],
           ["A. Black hole", "B. Milky Way", "C. Asteroid"],
           ["A. Mars", "B. Jupiter", "C. Uranus"],
           ["A. Black Hole", "B. Milky Way", "C. Earth"],
           ["A. Corona", "B. Star", "C. Earth"],
           ["A. Supernova", "B. Fusion", "C. Gravity"],
           ["A. Sputnik", "B. Sputnik", "C. Star 1"]]

new_game()

while play_again():
    new_game()

print("BYE!")