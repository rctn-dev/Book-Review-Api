# Book-Review-Api
Book Review Api: Django Rest Framework with Faker and Requests Library
Models: Book, Comment, User
API Endpoints:
   api/book-view/                  # list and create action methods
   api/book-view/<int:pk>/         # retrieve, update, and destroy action methods
   api/comment-view/<int:pk>/      # retrieve, update, and destroy action methods
   api/book-view/<int:pk>/comment/ # create action method
   
Some Specs:
* One-to-many(Foreign Key) relation models including built-in User model.
* Validators as a model field attribute.
* Nested ModelSerializers with the use of related_name model attribute preventing integrity error, and 
  StringRelatedField for better naming.
* Generics class with perform_create overwrite.
* Built-in and Custom Permissions
* Preventing multiple comments from the same user.
* A user can see only its own comment.
* Pagination
* Populating User and Book models using Faker and requests library.(fake_data.py in scripts folder)
  
Some Important Notes:
For the User model, the creation is not handled by endpoint, use either fake_data script or create manually by using the admin panel.
There is a pipfile for fast-installing the related libraries, it is better you install pipenv, which combines pip and venv, and use it to install libraries within the terminal,such as
>> pipenv install
The command above will automatically install all necessary libraries.
Before starting the  server with the following command, amke sure you employ the python interpreter inside the virtual environment.
>> python manage.py runserver
It is easier you populate the User database with admin panel.
Since endpoints can be used by authenticated users, make sure you login with one of the users.
