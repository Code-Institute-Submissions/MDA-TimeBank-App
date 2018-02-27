def username(name):
    return name

def check_username(name):
    while True:
        if len(name) < 1:
            name = input("Your username cannot be blank. Reveal yourself: ")
            continue
        return name