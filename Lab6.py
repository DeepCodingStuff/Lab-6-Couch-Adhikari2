#Lab 6
#Cayden Couch and Deep A.


def encode(encoded_password):
    password = input("Please enter your password to encode: ")
    encoded_password = ""
    for i in password:
        encoded_num = (int(i) + 3) % 10
        encoded_password += str(encoded_num)
    print("Your password has been encoded and stored!")


def main():
    encoded_password = ""
    run = True
    while run:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("Please enter an option: ")
        if option == 1:
            encode(encoded_password)
        elif option == 2:
            pass
        else:
            run = False


