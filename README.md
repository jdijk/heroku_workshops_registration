# Heroku Workshops Registration
### Allow invitees to register to a workshop then scan the emailed QR code to track attendance

- - -


#### Workflow:

1. Login to http://your_app_url/admin
2. Create a new Workshop record - slug should be in a URL friendly format such as: work_another_word
3. Send emails to invitee list using Salesforce or other means, pointing invitees to: http://your_app_url/workshop/your_workshop_slug
4. Invitees fill out the form
5. Back in the Admin you can see the registrations
6. Invitees get a confirmation email (from Sendgrid) with a QR Code
7. Use a QR Scanning app to scan it - QR Code represents an endpoint which will mark that ateendee as attended.


#### Running on Heroku

1. Create an app on Heroku
2. Add Postgres add-on
3. Add SendGrid add-on
4. Add a web dyno and a worker dyno
5. Clone this repository and push it to your new Heroku app
6. Now do a few Heroku runs to set up the database for Django:

```bash
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

#### Running locally

1. Get a [Google Recaptcha Key](https://www.google.com/recaptcha/intro/)
2. Get a [Sendgrid Key](https://elements.heroku.com/addons/sendgrid)
3. Add a file called dev.py to app_folder/projherokureg and set 2 variables with the relevant values. These will be environment variables in Heroku.
    * RECAPTCHA_SECRET_KEY
    * SENDGRID_KEY
2. Get [Docker](https://www.docker.com/)
2. Get [Docker-Compose](https://docs.docker.com/compose/)
3. Run docker-compose up in the main directory
4. Most often it fails the first time - Ctrl + c and run it again - should be fine 2nd time.
5. Now you need to set up the DB, only need to do this once:

```bash
docker exec -it herokuworkshopreg_web_1 bash
$> python manage.py migrate
$> python manage.py createsuperuser (follow prompts)
$> Ctrl + d to close
```