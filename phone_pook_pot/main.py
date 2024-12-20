from contacts import add_birthday, add_contact, birthdays, change_contact, show_birthday, show_phone, show_all
from adress_book import AddressBook  

    
def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        command = input("Enter a command: ").lower().strip()
        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                args = input("Enter name and phone: ").split()
                print(add_contact(args, book))
            case "change":
                args = input("Enter name and new phone: ").split()
                print(change_contact(args))
            case "phone":
                args = input("Enter name: ").split()
                print(show_phone(args, book))
            case "all":
                print(show_all(book))
            case "add-birthday":
                args = input("Enter birthday: ").split()
                print(add_birthday(args, book))
            case "show-birthday":
                print(show_birthday(args, book))
            case "birthdays":
                print(birthdays(args, book))
            case _:
                print("Invalid command.")

if __name__ == "__main__":
    main()