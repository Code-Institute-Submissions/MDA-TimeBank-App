"""
REGISTER FUNCTION
"""
def validate_username(username):
    # username = (input("Create a username: "))
    while True:
        if len(username) < 1:
            username = input("Your username cannot be blank. Reveal yourself: ")
            continue
        return username
    
def validate_email_address(email):
    # email = input("What is your email address? ")
    while True:
        if len(email) < 6:
            email = input("That's not a valid email address.\nWe'll only use this to notify you of MDA events and opportunities.\nTry again:")
        if "@" and "." not in email:
            email = input("Your email address must contain a '@' and a '.'\nWe'll only use this to notify you of MDA events and opportunities.\nTry again:")
            continue
        return email

"""
QUESTIONS_ANSWERS FUNCTION
"""
def ask_questions(guess, answer):
    if guess is str(guess):
        return 0
    elif int(guess) == int(answer):
        return 10
    elif ((guess > answer) and (guess < (answer + 10))) or ((guess < answer) and (guess > (answer - 10))):
        return 5
    else:
        return 0
   
   