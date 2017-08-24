
def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
                 'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
                 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    username = get_username()
    check_username(username, usernames)


def get_username():
    username = input("what is your name? :")
    return username


def check_username(username, usernames):
    if username in usernames:
        print("Access Granted")
    else:
        print("Access Denied")

main()
