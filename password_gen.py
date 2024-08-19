import random

def password_gen():

    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    SYMB = ['-', '/', '@', '?', '!', '&', '$', '#']
    CHARS = MAYUS + MINUS + NUMS + SYMB

    password = []

    for i in range(13):
        random_char = random.choice(CHARS)
        password.append(random_char)

    password = "".join(password)
    return password

def run():
    password  = password_gen()
    print(f"contraseña es {password}")

if __name__ == '__main__': run()