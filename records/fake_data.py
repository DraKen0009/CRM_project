from faker import Faker
from .models import Record
fake = Faker()

def create():
    for i in range(100):
        name=fake.name()
        country=fake.country()
        email=fake.ascii_safe_email()

        Record.objects.create(name=name,country=country,email=email,user_id=1)

