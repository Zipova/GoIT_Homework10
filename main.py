from collections import UserDict

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

class Record:
    def __init__(self, name, phone = None) -> None:
        self.name = name
        self.phones = []
        self.phones.append(phone)

    def add_phone(self, phone):
        self.phones.append(phone)
        return 'Done!'

    def del_phone(self, phone):
        for p in self.phones:
            if p.value == phone.value:
                self.phones = filter(lambda x: x != p, self.phones)
            return 'Done!'
        return "This phone doesn't exist in this contact."

    def edit_phone (self, phone, new_phone):
        for p in self.phones:
            if p.value == phone.value:
                p.value = new_phone.value
            return 'Done!'
        return "This phone doesn't exist in this contact."

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
        elif user_command.lower().startswith('delate '):
            print(delate(user_command, phone_book))

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
        all_phones = ''
        for p in v.phones:
            all_phones += str(p.value) + ', ' 
        result = result + f'{k} : {all_phones[:-2]}\n'
    return result[:-1]

@input_error
def add(user_command, phone_book):
    command = user_command.split(' ')
    if len(command) != 3:
        raise IndexError()
    name = Name(command[1])
    phone_number = Phone(int(command[2]))
    if name.value in phone_book.keys():
        rec = phone_book[name.value]
        rec.add_phone(phone_number)
        return 'Done!'
    rec = Record(name, phone_number)
    phone_book.add_record(rec)
    return 'Done!'


@input_error
def change(user_command, phone_book):
    command = user_command.split(' ')
    if len(command) != 4:
        raise IndexError()
    name = Name(command[1])
    phone_number = Phone(int(command[2]))
    new_phone = Phone(int(command[3]))
    if name.value not in phone_book.keys():
        raise KeyError()
    phone_book[name.value].edit_phone(phone_number, new_phone)
    return 'Done!'

@input_error
def delate(user_command, phone_book):
    command = user_command.split(' ')
    if len(command) != 3:
        raise IndexError()
    name = Name(command[1])
    phone_number = Phone(int(command[2]))
    if name.value not in phone_book.keys():
        raise KeyError()
    return phone_book[name.value].del_phone(phone_number)
    

@input_error
def phone(user_command, phone_book):
    command = user_command.split(' ')
    if len(command) != 2:
        raise KeyError()
    name = Name(command[1])
    all_phones = ''
    for p in phone_book[name.value].phones:
            all_phones += str(p.value) + ', ' 
    return (all_phones[:-2])


if __name__ == "__main__":
    main()