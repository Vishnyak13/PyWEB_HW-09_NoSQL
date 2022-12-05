import random

from faker import Faker

from mongo_db_assist.models import Contact

fake = Faker('uk_UA')


def fake_contacts(n):
    for _ in range(n):
        contact = Contact(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            phone=[sanitize_phone(fake.phone_number()) for _ in range(random.randint(1, 2))],
            email=[fake.email() for _ in range(random.randint(0, 2))],
            address=fake.address(),
            birthday=fake.date_of_birth(minimum_age=18, maximum_age=60),
            favorite=random.choice([True, False]),
            created_at=fake.date_time_between(start_date='-2y', end_date='now')
        )
        contact.save()
    return f'{n} fake contacts created!'


def sanitize_phone(phone):
    clear_phone = phone.strip().replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
    if clear_phone.startswith('380'):
        return f'+{clear_phone}'
    elif clear_phone.startswith('80'):
        return f'+3{clear_phone}'
    elif clear_phone.startswith('0'):
        return f'+38{clear_phone}'
    else:
        return f'{clear_phone}'
