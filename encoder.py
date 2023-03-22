def encode(password):
    newPass = ""
    for digit in password:
        newPass += str((int(digit) + 3))
    return newPass

def decode(password):
    newPass = ""
    for digit in password:
        newPass += str((int(digit) - 3))
    return newPass

def main():
    menu = True
    while menu:
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        num = int(input())
        if num == 1:
            password = input("Enter an 8 digit password of only integers.")
            print("You password has been encoded and stored!")
        elif num == 2:
            depassword = decode(password)
            print("The encoded password is ", password, ", and the orignal password is ", depassword,"." )
        else: 
            break

if __name__ =="__main__":
    main()