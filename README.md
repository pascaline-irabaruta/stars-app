<p>
<a href="https://wards-app.herokuapp.com/" target="_blank">
  <h1 align="center">Stars-App ...</h1>
</a>
</p>
An web application which allows a user to post a project he/she has created and get it reviewed by his/her peers and
and review the work submitted by his/her peers.
 A project can be rated based on 3 different criteria
1. Design
2. Usability
3. Content
## Technologies used

1. Python3
2. SQLite3
3. MDBootstrap 4.8.10
4. jQuery 3.4.1
5. Django 1.11.23

## Requirements

This project requires python3 to run

## Setting up a virtual environement

To create a virtual environement, you will need to install virtualenv
```sh
pip3 install virtualenv
```

Create the virtual environement by running the command in the project root
```sh
virtualenv venv
```

Activate the virtual environement by running the command
```sh
source venv/bin/activate
```

You can always deactivate the virtual environement by entering this command
```sh
deactivate
```

## Usage

Make migrations by using the command
```sh
python manage.py migrate
```

You need to create a .env file and set your secret key inside it. To launch the app, simply run the command
```sh
 python manage.py runserver
```

## Run tests

```sh
python manage.py test
```

## API
Users endpoint

```sh
https://wards-app.herokuapp.com/api/users/
```
Projects endpoint

```sh
https://wards-app.herokuapp.com/api/projects/
```
## Author

👤 **Pascaline Irabaruta**

* Github: [@pascyirabaruta](https://github.com/pascaline-irbaruta)
