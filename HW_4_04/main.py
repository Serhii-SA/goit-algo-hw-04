
text= ''' 
"add username phone".

 За цією командою бот зберігає у пам'яті, 
новий контакт. Користувач вводить ім'я username та номер телефону phone, обов'язково через пробіл.

"change username phone"
За цією командою бот зберігає в пам'яті новий номер телефону phone для 
контакту username, що вже існує в записнику.

"phone username"
 За цією командою бот виводить у консоль номер телефону для зазначеного контакту username.

"all"
 За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль.

"close", "exit"
 за будь-якою з цих команд бот завершує свою роботу
 '''

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    
    if 1<len(args)<3:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    else:
        return "Invalid input"

def chng_contact(args, contacts):
    if 1<len(args)<3:
        name, phone = args
        contacts[name] = phone
        return f"Contact {name} phone number was changed(or added in case of not exist)."
    else:
        return "Invalid input"   

def all_contact(contacts):
    for key in contacts:
        print(key,contacts[key])

def usn_ph(args, contacts):
    try:
        print(args[0],contacts[args[0]])
    except:
        print(f"No user with name - {args[0]}")
    
        
def main():
    contacts = {}
    print("Welcome to the assistant bot!\n(\"Help\"-for help)")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?(\"Help\"-for help)")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "all":
            all_contact(contacts)
        elif command == "change":
            print(chng_contact(args, contacts))
        elif command == "phone":
            usn_ph(args, contacts) 
        elif command == "help":
            print(text)           
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

