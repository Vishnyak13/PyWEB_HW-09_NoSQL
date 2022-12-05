from mongo_db_assist.models import Contact
import datetime

from mongoengine.errors import NotUniqueError, ValidationError, DoesNotExist


def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NotUniqueError:
            return 'Phone or email already exist!'
        except ValidationError:
            return 'Invalid phone or email!'
        except DoesNotExist:
            print('Contact not found!')

    return wrapper


def handler_contact(contacts):
    for contact in contacts:
        phones = ', '.join([phone for phone in contact.phone]) if contact.phone else 'No phone number'
        emails = ', '.join([phone for phone in contact.email]) if contact.email else 'No email'
        print(f'Name: {contact.full_name}, Phone: {phones}, Email: {emails}, Address: {contact.address}, ' \
              f'Birthday: {contact.birthday}, Created at: {contact.created_at}')


def get_all_contacts():
    contacts = Contact.objects()
    return handler_contact(contacts)


def get_contact_by_name(name):
    contacts = Contact.objects(first_name=name)
    return handler_contact(contacts)


def get_favorite_contacts():
    contacts = Contact.objects(favorite=True)
    return handler_contact(contacts)


def remove_contact(first_name, last_name):
    contact = Contact.objects.get(first_name=first_name, last_name=last_name)
    contact.delete()
    return f'Contact {contact.full_name} removed from database!'


@exception_handler
def add_contact(**kwargs):
    contact = Contact(**kwargs)
    contact.save()
    return f'Contact {contact.full_name} added to database!'


@exception_handler
def update_contact(**kwargs):
    contact = Contact.objects.get(first_name=kwargs['first_name'], last_name=kwargs['last_name'])
    if kwargs.get('phone'):
        contact.phone = list(kwargs['phone'])
    if kwargs.get('email'):
        contact.email = list(kwargs['email'])
    if kwargs.get('address'):
        contact.address = kwargs['address']
    if kwargs.get('birthday'):
        contact.birthday = datetime.datetime.strptime(kwargs['birthday'], '%Y-%m-%d')
    if kwargs.get('favorite'):
        contact.favorite = kwargs['favorite']
    contact.save()
    return f'Contact {contact.full_name} updated!'
