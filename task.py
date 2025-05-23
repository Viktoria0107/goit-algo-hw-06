from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
		pass

class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            self.value = value
        else:
            raise ValueError("Ten signs are expected")
            
    
   

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу
    def add_phone(self, number_phone):
        phone = Phone(number_phone)
        self.phones.append(phone)

    def remove_phone(self, number_phone):
        self.find_phone(number_phone)
        return self.phones.remove(number_phone)
    

    def edit_phone(self, number_phone, new_number_phone):
        phone = self.find_phone(number_phone)
        if phone:
            self.add_phone(new_number_phone)
            self.phones.remove(phone)
        else:
            raise ValueError("Enter the phone number again") 
           


    def find_phone(self, number_phone):
        for phone in self.phones:
            if phone.value == number_phone:
                return phone   
        return None
    
        

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find (self, name):
        return self.data.get(name)


    def delete (self, name):
        del self.data[name]


    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())


 




# Створення нової адресної книги
book = AddressBook()

    # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
book.add_record(john_record)

    # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

    # Виведення всіх записів у книзі
     
print(book)

    # Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1122233333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі Jo
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

    # Видалення запису Jane
book.delete("Jane")