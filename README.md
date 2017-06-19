# Heroku Workshops Registration
### Allow invitees to register to a workshop then scan the emailed QR code to track attendance

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/feliperyan/heroku_workshops_registration)

- - -

#### How to use the app:

1. Login to http://your_app_name.herokuapp.com/admin
2. Create a new Workshop record - slug should be in a URL friendly format such as: this-is-my-event
3. Now you can start inviting people to the event! The registration form is at: http://your_app_name.herokuapp.com/workshop/your-event-slug
4. Use Salesforce to email your invitees (or another tool)
5. Back in the Admin you can see the registrations!
6. Invitees get a confirmation email (from Sendgrid) with a QR Code
7. When hosting the event, Use a QR Scanning app on your mobile and reques the code from the attendees, the attendance will be marked back in the app, you can view it in the admin!

#### Running on Heroku

1. Deploy using the Heroku Button!
2. Get a [Google Recaptcha Key](https://www.google.com/recaptcha/intro/)
3. Get a [SendGrid Api key](https://devcenter.heroku.com/articles/sendgrid#obtaining-an-api-key)
4. Add both the recaptcha and the sendgrid keys to the Config Vars under Settings in Heroku
5. Follow the instructions above on how to use the app - **the default admin/password is: adminuser/admin001**

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