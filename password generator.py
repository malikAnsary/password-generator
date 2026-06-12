import random
import string


def chooseMode():
    print("1. digits\n2. letters\n3. complex")
    while True:
        try:
            mode = int(input("\nplease choose a mode -->"))
            if mode in (1, 2, 3):
                return mode
            else:
                print("choose only within the range of chocies")
        except:
            print("please try again")    


def makepassword():

    mode = chooseMode()
    cleanPrinties = "".join(string.printable.split())

    if mode == 1:
        passwordI = random.choices(string.digits, k=8)
    elif mode == 2:
        passwordI = random.choices(string.ascii_lowercase, k=8)
    else:
        passwordI = random.choices(cleanPrinties, k=8)

    return "".join(passwordI)

print(f"your password is:\n{makepassword()}")

