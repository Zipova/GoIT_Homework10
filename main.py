from collections import UserDict

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

class Record:
    def __init__(self, name, phone = None) -> None:
        self.name = name
        self.phone = phone
        
class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass

class Phone(Field):
    pass



def main():
    phone_book = AddressBook()
    while True:
        user_command = input('>>>')
        if user_command == '.':
            break
        elif user_command.lower() == 'hello':
            print(greeting())
        elif user_command.lower() in ("good bye", "close", "exit"):
            print(good_buy())
            break
        elif user_command.lower().startswith('add '):
            print(add(user_command, phone_book))
        elif user_command.lower().startswith('change '):
            print(change(user_command, phone_book))
        elif user_command.lower() == 'show all':
            print(show_all(phone_book))
        elif user_command.lower().startswith('phone '):
            print(phone(user_command, phone_book))
            

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'This name do not exist in your phone book!'
        except ValueError:
            return 'Please enter a phone number.'
        except IndexError:
            return 'Give me name and phone please.'
    return inner


def greeting():
    return 'How can I help you?'

def good_buy():
    return 'Good buy!'

def show_all(phones):
    result = ''
    for k, v in phones.items():
        result = result + f'{k} : {v.phone.value}\n'
    return result[:-1]

@input_error
def add(user_command, phone_book):
    command = user_command.split(' ')
    if len(command) != 3:
        raise IndexError()
    name = Name(command[1])
    phone_number = Phone(int(command[2]))
    rec = Record(name, phone_number)
    phone_book.add_record(rec)
    return 'Done!'


@input_error
def change(user_command, phone_book):
    command = user_command.split(' ')
    if len(command) != 3:
        raise IndexError()
    name = Name(command[1])
    phone_number = Phone(int(command[2]))
    if name.value not in phone_book.keys():
        raise KeyError()
    rec = Record(name, phone_number)
    phone_book.add_record(rec)
    return 'Done!'

@input_error
def phone(user_command, phone_book):
    command = user_command.split(' ')
    if len(command) != 2:
        raise KeyError()
    name = Name(command[1])
    return phone_book[name.value].phone.value


if __name__ == "__main__":
    main()