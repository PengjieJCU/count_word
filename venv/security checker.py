def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
    'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole',
    'InterpreterInterface', 'StartServer', 'bob']
    name = str(input("please enter your name"))
    if name in usernames:
        print("Access granted")
    else:
        print("Access denied")

main()
