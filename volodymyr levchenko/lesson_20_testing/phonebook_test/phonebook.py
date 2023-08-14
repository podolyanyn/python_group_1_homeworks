import json
import sys
import os

# file_name = sys.argv[1]
# print(sys.argv)


def read_data(file_name):
    with open(file_name, 'r') as file:
        if len(file.read()) == 0:
            return {}
        else:
            file.seek(0)
            return json.loads(file.read())


def change_data(file_name, details):
    with open(file_name, 'w') as file:
        json.dump(details, file)


def add_new_contact(file_name):
    phonebook = read_data(file_name)
    print("Enter following details to add new contact: ")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    number = input("Phone number: ")
    city = input("City: ")
    state = input("State: ")
    phonebook[number] = {"first_name": first_name.capitalize(),
                         "last_name": last_name.capitalize(),
                         "city": city.title(),
                         "state": state.title()
                         }
    change_data(file_name, phonebook)


def search_by_first_name(file_name):
    phonebook = read_data(file_name)
    first_name = input("First name: ").lower()
    os.system('cls')
    for num, data in phonebook.items():
        if data["first_name"].lower() == first_name:
            show_data(phonebook, num)
            break
    else:
        print("No such first name in the phonebook")


def search_by_last_name(file_name):
    phonebook = read_data(file_name)
    last_name = input("Last name: ").lower()
    os.system('cls')
    for num, data in phonebook.items():
        if data["last_name"].lower() == last_name:
            show_data(phonebook, num)
            break
    else:
        print("No such last name in the phonebook")


def search_by_full_name(file_name):
    phonebook = read_data(file_name)
    full_name = input("Full name: ").lower()
    os.system('cls')
    first_name = full_name.split(" ")[0]
    last_name = full_name.split(" ")[1]
    for num, data in phonebook.items():
        if data["first_name"].lower() == first_name and data["last_name"].lower() == last_name:
            show_data(phonebook, num)
            break
    else:
        print("No such name in the phonebook")


def search_by_phone_number(file_name):
    phonebook = read_data(file_name)
    number = input("Phone number: ")
    os.system('cls')
    if number in phonebook:
        for num in phonebook.keys():
            if num == number:
                show_data(phonebook, num)
    else:
        print("No such number in the phonebook")


def search_by_city_or_state(file_name):
    phonebook = read_data(file_name)
    city_or_state = input("City or state: ").lower()
    os.system('cls')
    for num, data in phonebook.items():
        if data["city"].lower() == city_or_state.lower() or data["state"].lower() == city_or_state.lower():
            show_data(phonebook, num)
            break
    else:
        print("No such city or state in the phonebook")


def delete_data_by_number(file_name):
    phonebook = read_data(file_name)
    number = input("Phone number: ")
    if number in phonebook:
        del phonebook[number]
        print(f"Contact with phone number {number} was deleted.")
    else:
        print("No such phone number in the phonebook")
    change_data(file_name, phonebook)


def update_data_by_number(file_name):
    phonebook = read_data(file_name)
    number = input("Phone number: ")
    if number in phonebook:
        first_name = input("First name: ")
        last_name = input("Last name: ")
        city = input("City: ")
        state = input("State: ")
        phonebook[number] = {"first_name": first_name.capitalize(),
                             "last_name": last_name.capitalize(),
                             "city": city.title(),
                             "state": state.title()
                             }
        print(f"Contact with phone number {number} was updated.")
    else:
        print("No such phone number in the phonebook")
    change_data(file_name, phonebook)


def show_data(phonebook, num):
    print(f"""First name: {phonebook[num]["first_name"]} 
Last name: {phonebook[num]["last_name"]}
Phone number: {num}
City: {phonebook[num]["city"]}
State: {phonebook[num]["state"]}
----------------------------""")


def show_phonebook(file_name):
    phonebook = read_data(file_name)
    if len(phonebook) == 0:
        print("Oops... Phonebook is empty")
    else:
        for num in phonebook.keys():
            show_data(phonebook, num)


def exit_program():
    print("Bye!")
    sys.exit()


def main_menu():
    choice = input("""Press option number to do an operation:
    1. Add new entries
    2. Search by...
    3. Delete a record for a given telephone number
    4. Update a record for a given telephone number
    5. Show the phonebook
    6. Exit the program   
    """)
    return choice


def search_by_menu():
    choice = input("""Press option number to do an operation:
    1. Search by first name
    2. Search by last name
    3. Search by full name
    4. Search by telephone number
    5. Search by city or state  
    6. Back 
    """)
    return choice


def press_any_key():
    input("Press any key to continue...")
    os.system('cls')


def main(file_name):
    phonebook = read_data(file_name)
    while True:
        main_choice = main_menu()
        if main_choice == '1':
            os.system('cls')
            add_new_contact(file_name)
            press_any_key()
        elif main_choice == '2':
            os.system('cls')
            search_choice = search_by_menu()
            if search_choice == '1':
                os.system('cls')
                search_by_first_name(file_name)
                press_any_key()
            elif search_choice == '2':
                os.system('cls')
                search_by_last_name(file_name)
                press_any_key()
            elif search_choice == '3':
                os.system('cls')
                search_by_full_name(file_name)
                press_any_key()
            elif search_choice == '4':
                os.system('cls')
                search_by_phone_number(file_name)
                press_any_key()
            elif search_choice == '5':
                os.system('cls')
                search_by_city_or_state(file_name)
                press_any_key()
            elif search_choice == '6':
                os.system('cls')
                continue
        elif main_choice == '3':
            delete_data_by_number(file_name)
            press_any_key()
        elif main_choice == '4':
            update_data_by_number(file_name)
            press_any_key()
        elif main_choice == '5':
            phonebook = read_data(file_name)
            os.system('cls')
            show_phonebook(file_name)
            press_any_key()
        elif main_choice == '6':
            os.system('cls')
            exit_program()


if __name__ == "__main__":
    os.system('cls')
    main(file_name)
