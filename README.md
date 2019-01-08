# Notes Keeper

A Notes WebApp built in Django using Python

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
* Run Django command to migrate database and run the server
```
$ python manage.py migrate
$ python manage.py runserver
```
The WebApp should be available at `http://127.0.0.1:8000`
