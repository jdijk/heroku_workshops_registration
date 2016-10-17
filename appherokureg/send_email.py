import sendgrid
import os
from sendgrid.helpers.mail import *
import qrcode
import io
import base64
from projherokureg.settings import SENDGRID_KEY


def send_notification(to_email, fullname, key):
    mail = prepare_email(to_email, fullname, key)
    do_it(mail)


def prepare_email(recipient, fullname, key):

    email_body = ('<html><body>'
    '<h1>Thank you for registering.</h1>'
    '<h3>Please find attached the QR Code to present at registration</h3>'+
    '</body></html>')

    from_email = Email('fryan@salesforce.com')
    subj = 'Hello ' + fullname + ' - Heroku Workshop'
    to_email = Email(recipient)
    content = Content('text/html', email_body)

    mail = Mail(from_email, subj, to_email, content)
    
    print(key)
    full_string = 'https://heroku-workshop-reg.herokuapp.com/attended/'+str(key)

    img = qrcode.make(full_string)
    b = io.BytesIO()
    img.save(b, format='PNG')
    s = b.getvalue()
    result = base64.b64encode(s).decode()

    a = Attachment()
    a.set_content(result)
    a.set_content_id('qr code')
    a.set_disposition('attachment')
    a.set_type('image/png')
    a.set_filename('code.png')

    mail.add_attachment(a)

    return mail


def do_it(the_mail):

    key = SENDGRID_KEY
    sg = sendgrid.SendGridAPIClient(apikey=key)
    res = sg.client.mail.send.post(request_body=the_mail.get())
    print(res.status_code)

