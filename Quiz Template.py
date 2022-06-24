def new_game():
    question_num = 1
    guesses = []
    correct_guess = 0

    for i in questions:
        print(i)
        for j in options[question_num - 1]:
            print(j)
        question_num += 1
        guess = input("Is the answer A, B, C, or D?: ").upper()
        guesses.append(guess)
        correct_guess += check_answer(questions.get(i), guess)
        print()
    display_score(correct_guess, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("Correct", end="")
        print(" -----------------------\n")
        return 1
    else:
        print("Incorrect", end="")
        print(" ---------------------\n")
        return 0


def display_score(correct_guess, guesses):
    score = int(correct_guess / len(guesses) * 100)

    print("------------------")
    print("GUESSES: ", end="")
    for i in guesses:
        print(i, end=" ")

    print()
    print("ANSWER:  ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print("\n------------------")

    print(f"\nYou got a {score}%. That is {correct_guess}/{len(guesses)} correct.")


questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is a tribute to which comedy group?: ": "C",
    "Is the earth round?: ": "A",
    "What is my name?: ": "D"
}

options = [
    ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    ["A. Lonely Island", "B. Smosh", "C. Month Python", "D. SNL"],
    ["A. True", "B. False", "C. Sometimes", "D. Never"],
    ["A. Tupac", "B. Obama", "C. Malcolm X", "D. Addie"]
]

# Main
new_game()
