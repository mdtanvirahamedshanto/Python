#           Question & Ans Game 
#           Write by Md Tanvir Ahamed Shanto


#------------------------
def new_game():
    
    guesse = []
    correct_guesse = 0
    question_num = 1

    for key in questions:
        print("------------------")
        print(key)
        for i in options[question_num -1]:
            print(i)
        guess = input("Enter Options (A,B,C or D): ")
        guess = guess.upper()
        guesse.append(guess)

        correct_guesse += check_answer(questions.get(key),guess)
        question_num += 1

    display_score(correct_guesse, guesse)
#------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT !")
        return 1
    else:
        print("WRONG !")
        return 0
#------------------------
def display_score(correct_guesse, guesse):
    print("--------------")
    print("RESULTS")
    print("------------------------")


    print("Answers: ",end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesse: ",end="")
    for i in guesse:
        print(i, end=" ")
    print()

    score = int((correct_guesse/len(questions))*100)
    print("Your Score is: "+str (score)+"%")
#------------------------
def play_again():
    response = input("Do You Play Again ? (Yes Or No): ")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False
#------------------------
questions = {
    "Who created Python ? ": "A",
    "What year was Python created ?": "B",
    "Python is tributed to which comedy group ?": "C",
    "Is the Earth round ?": "A"
}
options = [["A. Guido van Rossum","B. Elon Musk","C. Bill Gates", "D. Mark Zuckerburg"],
           ["A. 1989","B. 1991","C. 2000", "D. 2016"],
           ["A. Lonely Island","B. Smosh","C. Monty Python", "D. SNL"],
           ["A. True","B. False","C. Sometimes", "D. What's Earth ?"]]
#-------------------------
new_game()

while play_again():
    new_game()

print("Byeeeeeeee..........")
print("Thanks For Playing")