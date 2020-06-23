# program only accepts typing in the number 2, because why not?

string = input("Write the character 2 only, as many times as you want: ")

for i in range(len(string)):
    if string[i] == "2":
        print(f"Yay, you typed in {len(string)} 2s")
    else:
        print("You suck")
        raise SyntaxError("Follow instructions lol")
