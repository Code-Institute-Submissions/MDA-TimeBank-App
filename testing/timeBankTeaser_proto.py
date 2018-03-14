"""
REGISTRATION FUNCTIONALITY
"""
def register():
    def check_email_contains(email_address, characters, min_length=6):
        while True:
            for character in characters:
                if character not in email_address:
                    email_address = input("Your email address must have '{}' in it\nPlease write your email address again: ".format(character))
                    continue
            if len(email_address) <= min_length:
                email_address = input("Your email address is too short.\nPlease write your email address again: ")
                continue
            return email_address
    
    def check_username(username, min_length=1):
        while True:
            if len(username) < min_length:
                username = input("Your username can't be empty.\nTry again: ")
                continue
            return username
            
    print("Please provide the following details to progress.")
    username = check_username(input("username: "))
    email_address = check_email_contains(input("What is your email address? "), "@.")
    file = open("user_info.txt", "a")
    file.write(username + "\n") 
    file.write(email_address + "\n") 
    file.close()     
    print("This information will only be used to notify you of any upcoming MDA projects and events.")


"""
SHOW MENU FUNCTION
"""
def show_menu():
    # print("Welcome, {0}. Take your pick: ".format(username))
    print("1. What is a TimeBank?")
    print("2. What do you think? Add your comments")
    print("3. Send me through to MDA's website please")

    option = input("Enter option: ")
    return option


"""
ASK QUESTIONS FUNCTION
"""
def ask_questions():
    questions = []
    answers = []

    with open("questions.txt", "r") as file:
        lines = file.read().splitlines()

    for i, text in enumerate(lines):
        if i%2 == 0:
            questions.append(text)
        else:
            answers.append(text)
    
    number_of_questions = len(questions)
    questions_and_answers = zip(questions, answers)
    
    score = 0
    
    for question, answer in questions_and_answers:          
        guess = input(question + "> ")
        if guess == answer:
            score += 1
            print("Spot on. No flies on you!")
            print("So far you've got {0} correct out of {1}".format(score, number_of_questions))
            print("")
            
            """ADD FUNCTIONALITY IN HERE FOR DIFFERENT RESPONSES (FILE) & TWO GUESSES
            This will not run - will run in replit as answer varaible defined. 
            Something to do wit the type conversion of answer variable and 
            performing math operation on it
            """
            
        # elif (guess answer + 10) and (guess >= answer +1):
        #     score += 1
        #     print("Close enough")
        #     print("So far you've got {0} correct out of {1}".format(score, number_of_questions))
        #     print("")
        
        else:
            print("Wrong!")
            print("So far you've got {0} correct out of {1}".format(score, number_of_questions))
            print("")
    
    print("TOTAL: You got {0} correct out of {1}".format(score, number_of_questions))
    

"""
ADD COMMENT FUNCTION
"""
def add_comment():
    print("")
    comment = input("What do you think?\n> ") 
    
    """INCLUDE VERIFICATION"""
    """LINK TO NOTICE BOARD"""
    
 
    file = open("comments.txt", "a")
    file.write(comment + "\n") 
    """INCLUDE TIME STAMP AND NAME"""
    
    file.close()     

"""
GAME LOOP FUNCTION
"""
def game_loop():
    register()
    while True:
        option = show_menu()
        if option == "1":
            ask_questions()
        elif option == "2":
           add_comment()
        elif option == "3":
            break
        else:
            print("Choose 1, 2 or 3 please. It's a bit like Stormont. Can't handle much more than multiple choice!")


game_loop()


 