# Notes Keeper

A Notes WebApp built in Django using Python. Live App on https://django-notes-keeper.herokuapp.com 

## Features
* Ability to Create, Edit, and Delete Notes.
* The Notes use an easy to use WYSIWYG Editor.
* Ability to make Public Notes, so anyone with the link can view it. (Private Notes can only be seen by the Author)
* User System with Password Hashing and Salting.

## Installation
* Clone the repository
```
$ git clone https://github.com/sggts04/notes-keeper
$ cd notes-keeper
```
* Edit config.json to change the secret key    
##### config.json
```
{
	"SECRET_KEY": "key_goes_here"
}
```
* Install Requirements, and run Django commands to migrate database, collect static, and run the server
```
$ pip install -r requirements.txt
$ python manage.py collectstatic
$ python manage.py migrate
$ python manage.py runserver
```
The WebApp should be available at `http://127.0.0.1:8000`

## Screenshots
* Dashboard
![](/screenshots/dash.PNG?raw=true)

* View Note
![](/screenshots/view.PNG?raw=true)

* New Note
![](/screenshots/new.PNG?raw=true)
