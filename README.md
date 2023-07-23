# Book-Review-Api
* **Book Review Api**: Django Rest Framework with Faker and Requests Library
* **Models**: Book, Comment, User
* **API Endpoints**:
   - api/book-view       
   - api/book-view/{bookId} 
   - api/comment-view/{commentId}
   - api/book-view/{bookId}/comment
* Built-in sqlite database is NOT populated. You can populate it with the admin panel as a superuser.    
```console
   PS: > python manage.py makemigrations  
   PS: > python manage.py migrate  
   PS: > python manage.py createsuperuser
```
**Some Specs**:
* One-to-many(Foreign Key) relation models including built-in User model.
* Validators as a model field attribute.
* Nested ModelSerializers with the use of _related_name_ model attribute preventing integrity error, and 
  _StringRelatedField_ for better naming convention.
* Generics class with _perform_create_ overwrite.
* Built-in and Custom Permissions
* Preventing multiple comments from the same user.
* A user can see only its own comment.
* Pagination
* Populating User and Book models using **Faker** and **requests** library.(fake_data.py in scripts folder)
  
**Some Important Notes**:
* For the _User_ model, the user creation is not handled by the endpoint, use either _fake_data.py_ script or the admin panel to create it.
There is a **pipfile** for fast-installing the related libraries, for which you need to install _pipenv_ first, which combines the functionalities of _pip_ and _venv_. The command above will automatically install all necessary libraries. 
```console
   PS: > pipenv install
```
* Before starting the  server with the following command, make sure you use the python interpreter that belongs to the virtual environment you created.
```console
   PS: > python manage.py runserver
```
*  Make sure you login first before using the endpoints since they ask for authentication.
