from cleaner import neocities

function_dict = {"neocities":neocities,"syntax":print("Syntax: [command] [arg1] NOTE: Ignore the brackets '[]'")}

while True:
    INPUT = str(input("COMMAND: "))
    k = len(INPUT.split())
    print(k)
    if k != 1:
        command = INPUT.split(' ')[0]
        print(command) 
        arg1 = INPUT.split(' ')[1]
        print(arg1)
    else:
        command = str(INPUT.split())
    if command in str(function_dict):
        response = function_dict[command](str(arg1))
        print(str(response))
    else:
        print("INVALID")