from pprint import pprint
from collections.abc import Iterable
import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE','BookBlogPro.settings')
import django 
django.setup()

# In order to write the following import, we need the statements above.
from django.contrib.auth.models import User 
from faker import Faker
import requests
from pprint import pprint 
from BookBlogApp.api.serializers import BookSerializer
# language selection
fake=Faker(['en_US'])

def set_user():
    f_name=fake.first_name()
    l_name=fake.last_name()
    u_name=f'{f_name}_{l_name}'
    email=f'{u_name}@{fake.domain_name()}'
    #uniqueness check for the username
    user_check=User.objects.filter(username=u_name)
    while user_check.exists():
        u_name=u_name + str(random.randrange(1,99))
        user_check=User.objects.filter(username=u_name)
    user=User(
        username=u_name, 
        first_name=f_name, 
        last_name=l_name,
        email=email,
        # ensuring 50% is true.
        is_staff=fake.boolean(chance_of_getting_true=50)
    )
    user.set_password('testing123..')
    user.save()
    print(f'A new user is registered: {user.username}')

def add_book(subject):
    # url='https://openlibrary.org/search.json?q=love'
    url='https://openlibrary.org/search.json'
    payload={'q':subject}
    response=requests.get(url, params=payload)
    if response.status_code!=200:
        print('Bad Request', response.status_code)
    response_jsn=response.json()
    books=response_jsn.get('docs')
    for book in books: 
        book_title=book.get('title')
        data={ 
            'title':book.get('title'),
            'author':book.get('author_name')[0],
            'description':iter_to_str(book.get('subject_key')),
            'price':round(random.randint(1000, 2000)/100, 2),
            'date_released':fake.date_time_between(start_date='-10y',end_date='now',tzinfo=None),

        }
        
        serialized_data=BookSerializer(data=data)
        if serialized_data.is_valid():
            serialized_data.save()
            pprint(f'the book:{book_title} is registered')
        else:
            continue
def iter_to_str(itr):
    res='_'
    if itr:
        for item in itr: 
            res+=item
        return res
    else:
        return None
        

