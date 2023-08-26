def command_parser(user_input):
            list = user_input.split()
            if list[0] == "good" and list[1] == "bye":
                return list[0] + " " + list[1], list[2:]
            elif list[0] == "show" and list[1] == "all":
                return list[0] + " " + list[1], list[2:]
            else:
                return list[0], list[1:]



def input_error(func):
    def inner(command):
        if inner == func_to_show_all or inner == func_to_hello or inner == func_to_exit:
            try:
                return func(command)
            except TypeError:
                return "You wrote wrong command, please, try again!"
        elif inner == func_to_add or inner == func_to_change:
            try:
                return func(command)
            except IndexError:
                return "Give me name and phone please after command."
        elif inner == func_to_phone:
            try:
                return func(command)
            except IndexError:
                return "Enter user name after command."
            except KeyError:
                return "You don't have this contact."
    return inner
        

@input_error
def func_to_show_all(data):
    if not data:
        return INFO_ABOUT_USERS
    else:
        raise TypeError

@input_error
def func_to_phone(data):
    if len(data) == 1:
        if data[0].title() in INFO_ABOUT_USERS:
            return f"Number for contact: {data[0].title()} is: {INFO_ABOUT_USERS[data[0].title()]}"
        else:
            raise KeyError
    else:
        raise IndexError


@input_error
def func_to_add(data):
    if len(data) == 2:
        INFO_ABOUT_USERS[data[0].title()] = data[1]
        return f"Your name: {data[0].title()} and phone: {data[1]} was saved."
    else:
        raise IndexError

@input_error
def func_to_change(data):
    if len(data) == 2:
        INFO_ABOUT_USERS[data[0].title()] = data[1]
        return f"You changed a phone. Contact: {data[0]} has a new phone: {data[1]}"
    else:
        raise IndexError

@input_error
def func_to_hello(data):
    if not data:
        return "How can I help you?"
    else:
        raise TypeError

@input_error
def func_to_exit(data):
    if not data:
        global active_bot
        active_bot = False
        return "Good bye!"
    else:
        raise TypeError


INFO_ABOUT_USERS = {}
active_bot = True

def main():
    global active_bot
    while active_bot:
            

        DICT = {
            "exit": func_to_exit,
            "good bye": func_to_exit,
            "close": func_to_exit,
            "hello": func_to_hello,
            "add": func_to_add,
            "show all": func_to_show_all,
            "change": func_to_change,
            "phone": func_to_phone
        }

        
        def handler(command):
            return DICT[command]
                 



        


        user_input = input("Please, write a command: ")
        user_input = user_input.lower()
        if user_input == "":
             print("Sorry, but you didn't write a command. Please, try again!")
             continue


        command, person_info = command_parser(user_input)

        try:
            function_to_work_with = handler(command)
            res = function_to_work_with(person_info)
            print(res)
        except:
             print("You wrote wrong command. Please, try again!")

        

if __name__ == "__main__":
     main()