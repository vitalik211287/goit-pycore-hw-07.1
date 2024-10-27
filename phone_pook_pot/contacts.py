from error_handler import input_error


contacts = {}


# @input_error
# def add_contact(args):  
#     # Додає контакт до словника.
#     name, phone = args  
#     contacts[name] = phone  
#     return f"Contact {name} added."  

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message



@input_error
def change_contact(args):  
    name, new_phone = args  
    if name in contacts:  
        contacts[name] = new_phone  
        return f"Contact {name} updated."  
    else:
        raise KeyError 

@input_error
def show_phone(args):  
    # Показує номер телефону для вказаного контакту.
    name = args[0]  
    if name in contacts:  
        return f"{name}'s phone number is {contacts[name]}."  
    raise KeyError

@input_error
def show_all():  
    # Показує всі контакти. 
    if contacts:  
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])  
    else:  
        return "No contacts found."  