import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','exercise1.settings')

django.setup()


##Fake pop scripts

import random
from appTwo.models import users
from faker import Faker



def populate(N=5):
    for entry in range(N):

        # Create an instance of the Faker class
        fake = Faker()

        # Generate a unique random first name
        first_name = fake.first_name()
        while users.objects.filter(firstName=first_name).exists():
            first_name = fake.first_name()

        
        # Generate a random last name

        last_name = fake.last_name()
        
        while users.objects.filter(lastName=last_name).exists():
            last_name = fake.last_name()
        

        fake_url=fake.url()

        #Create the new user entry
        webpg=users.objects.get_or_create(firstName=first_name,eMail=fake_url, lastName=last_name)[0]

        webpg.save()
    return webpg


if __name__=='__main__':
    print("Populating Script")
    populate(20) 
    print("Populating Complete ")
        
