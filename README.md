# Event-Controller

This project was made as a part of Inoa's internship process.

## Install

```bash
git clone https://github.com/brenorosas/Event-Controller.git
cd inoa-challenge
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

After installing, it is also needed to use the .env.example to create a new .env file with the data filled in:

```bash
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DJANGO_KEY=Your django secret key
EMAIL_ADDRESS="example@gmail.com"
EMAIL_PASSWORD=Your gmail password
```

If you have two factor authentication in your gmail account, use an [app password](https://support.google.com/accounts/answer/185833).

You maybe also need to permit access to apps with lower security on your gmail account.

## Run

To run the app, `docker` and `docker-compose` must be installed on your system. For installation
instructions refer to the Docker [docs](https://docs.docker.com/compose/install/). 

#### Compose
The app can be run in development mode using Django's built in web server simply by executing

```bash
docker-compose up
```

To remove all containers in the cluster use

```bash
docker-compose down -v
```
You can see the site on your browser accessing localhost:8000
## Functionalities
#### Home Page
Just the name of project.

#### Registering account
Click on "Register", insert your datas and submit, if everything is okay you will be redirectioned to home page.

#### Logging in
Click on "Login", insert your datas that you have already created, if everythin is okay you will be redirectioned to your profile.

#### Viewing profile
If you're logged in, there will be an option options to see your Events, add an event, see your guests and add guests.

#### Viewing all events
Being logged in, click on the "Events" option to view your created events. You can also click on the Event to see more details. You also can filter your events.

#### Adding events
Being logged in, click on the "Add Event", you will need to insert some informations about the Event, Name, Slug, Description and Date. The name and the Description will be used in the emails to the guests.

#### Viewing guests
Here you can just see all the guests you have to all your events. Name of guest, email of guest e which event he was invited.

#### Adding guests
Here you will need to insert the Name and email of the guest, and select the event to invite him. If everythin is okay and the email was send to the guest, you will be redirectioned to your events page.