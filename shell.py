command_list = ["read"]

while True:
    INPUT = str(input("COMMAND: "))
    if INPUT in command_list:
        print(INPUT)
    else:
        print("INVALID")