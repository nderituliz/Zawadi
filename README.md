# Zawadi App
## Author
Liz Nderitu

## Live Link


## Description
 Zawadi is a project made to enable users to register and post their projects. The users can also rate other existing projects on the website based on design, usability and content.

## User Stories
What the user does...
* A user can view posted projects and their details.
* A user can post a project to be rated/reviewed.
* A user can rate/ review other users' projects.
* Search for projects.
* View projects overall score.
* A user can view their profile page.

## Installation / Setup instruction
One can follow the following steps to get the project .......
#### The application requires the following installations to operate 
* python3
* pip

### Navigate into the folder and install requirements
```cd project-awwards pip install -r requirements.txt ```

### Install and activate Virtual
```- python3 -m venv virtual - source venv/bin/activate ```

### Setup Database
SetUp your database User,Password, Host then make migrate
```python manage.py makemigrations```
```python manage.py migrate ```

### Run the application
```python manage.py runserver ```

### Testing the application
```python manage.py test ```



## Behaviour Driven Development
| Input | Output | Behaviour |
| :---------------- | :---------------: | ------------------: |
|Visit awwards-clone site| Various projects are displayed|User can review projects|
|Click on image| Image details displayed| Image details displayed|
|Search project| Images for project are displayed|  App gets the projects for the searched project|
|Visit profile| Projects posted by user are displayed|App gets projects for user|
|Visit Admin |Prompts for admin credentials|Admin dashboard displayed|
|API projects|api with a list of projects is displayed| api displayed|


## Technologies Used

* python3
* Django
* Bootstrap
* HTML / CSS
* Postman for visual representation while building the api


## Known Bugs
* There are no known bugs at the moment

## Contact Information 

If you have any question or contributions, please email me at [nderituliz@gmail.com]

## License
* [[License: MIT]](LICENCE.md)
* Copyright (c) 2021 **Liz Nderitu**
