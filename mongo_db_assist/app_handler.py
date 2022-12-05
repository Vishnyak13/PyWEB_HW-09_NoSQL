from mongo_db_assist.seed import get_all_contacts, get_contact_by_name, get_favorite_contacts, remove_contact, add_contact, \
    update_contact
from mongo_db_assist.fake_data import fake_contacts


def match_case(choice):
    match choice:
        case 1:
            get_all_contacts()
        case 2:
            get_contact_by_name(input('Enter name: '))
        case 3:
            get_favorite_contacts()
        case 4:
            print(remove_contact(input('Enter first name: '), input('Enter last name: ')))
        case 5:
            print(add_contact(first_name=input('Enter first name: '), last_name=input('Enter last name: '),
                              phone=map(str, input('Enter phone: ').split(',')),
                              email=map(str, input('Enter email: ').split(',')),
                              address=input('Enter address: '), birthday=input('Enter birthday (YYYY-MM-DD): '),
                              favorite=input('Enter favorite (True/False): ')))
        case 6:
            print(update_contact(first_name=input('Enter first name: '), last_name=input('Enter last name: '),
                                 phone=map(str, input('Enter phone: ').split(',')),
                                 email=map(str, input('Enter email: ').split(',')),
                                 address=input('Enter address: '), birthday=input('Enter birthday (YYYY-MM-DD): '),
                                 favorite=input('Enter favorite (True/False): ')))


def run():
    try:
        while True:
            print('What do you want to do?')
            print('1. Get all contacts')
            print('2. Get contact by name')
            print('3. Get favorite contacts')
            print('4. Remove contact')
            print('5. Add contact')
            print('6. Update contact')
            print('7. Exit')
            choice = int(input('>>>: '))
            if choice == 7:
                print('Goodbye!')
                break
            match_case(choice)
    except ValueError:
        print('Please enter a number')
        run()


def app_handler():
    print('Welcome to Address Book')
    print('Do you want to create fake contacts? (y/n)')
    if input('>>>: ') == 'y':
        print('How many contacts do you want to create?')
        print(fake_contacts(int(input('Enter count: '))))
        run()
    else:
        print('Ok, no fake contacts')
        run()
