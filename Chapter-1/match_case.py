# Match Case Program
'''
n = int(input("enter a number : "))
match n:
    case 0:
        print("number is zero")
    case 1:
        print("number is one")
    case 2:
        print("number is two")
    case 3:
        print("number is three")
    case 4:
        print("number is four")
    case _:
        print("number is ",n)
'''
# Check 
x = input("enter True and False if you are going for vote : ").capitalize()
match x:
    case "True":
        print("Who you are going to vote 🧐? : ")
        y = input("enter a party name (kitty or bitchy)? : ")
        match y:
            case "kitty":
                print("you are going to vote kitty party 😻")
            case "bitchy":
                print("you are going to vote bitchy party 👧")
    case "False":
        print("you are not going to vote ? why ? : ")
        z = int(input("enter your age : "))
        match z:
            case _ if (z <= 18):
                print("ohh you are nihal bitch!! 🦋")
            case _ if (z > 18):
                print("ohh you are definetly love kirat!! 👨")
