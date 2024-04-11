from cleaner import neocities

function_dict = {"neocities":neocities}

while True:
    INPUT = str(input("COMMAND: "))
    k = len(INPUT.split())
    print("Lenght:" + k)
    command = INPUT.split(' ')[0]
    print("Command: " + command) 
    arg1 = INPUT.split(' ')[1]
    print("Argument: " + arg1)
    if command in str(function_dict):
        response = function_dict[command](str(arg1))
        print(str(response))
    else:
        print("INVALID")