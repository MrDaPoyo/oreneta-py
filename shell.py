from cleaner import neocities

function_dict = {"neocities":neocities}

while True:
    INPUT = str(input("COMMAND: "))
    command = INPUT.split(' ')[0]
    print(command) 
    arg1 = INPUT.split(' ')[1]
    print(arg1)
    if command in function_dict:
        response = function_dict[command](str(arg1))
        print(str(response))
    else:
        print("INVALID")