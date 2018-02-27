def username(name):
    return name

def validate_username(name):
    while True:
        if len(name) < 1:
            name = input("Your username cannot be blank. Reveal yourself: ")
            continue
        else:
            return name

def email_address(email):
    while True:
        if len(email) < 6:
            email = input("That's not a valid email address.\nWe'll only use this to notify you of MDA events and opportunities.\nTry again:")
            continue
        if "@" and "." not in email:
            email = input("Your email address must contain a '@' and a '.'\nWe'll only use this to notify you of MDA events and opportunities.\nTry again:")
            continue
        else:
            return email

