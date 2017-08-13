import os
from django.conf import settings
from django.template.loader import render_to_string
import boto.ses


class EmailerAPI():

    email_source = 'no-reply@inroad.co'

    def get_connection(self):

        conn = boto.ses.connect_to_region('us-east-1', aws_access_key_id=settings.AWS_ACCESS_KEY_ID, aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

        return conn


    def verify_sender(self, email_address):

        conn = self.get_connection()

        return conn.verify_email_address(email_address)


    def send_email(self, params):
        conn = self.get_connection()

        html_body = render_to_string('email/html/%s.html' % params['template'], params)
        text_body = render_to_string('email/text/%s.txt' % params['template'], params)

        conn.send_email(source=self.email_source,
                        subject = params['subject'],
                        to_addresses = params['to_address'],
                        reply_addresses = self.email_source,
                        format='html',
                        body=html_body,
                        text_body=text_body)


    def list_verified_email(self):
        conn = self.get_connection()

        return conn.list_verified_email_addresses()


class Emailer():

    emailer = EmailerAPI()

    def __init__(self):
        pass

    def send_welcome_email(self, params):

        params['subject'] = "You're almost done!"
        params['template'] = 'welcome'

        self.emailer.send_email(params)

    def send_validation_email(self, params):
        params['subject'] = "validate email"
        params['template'] = 'validate_email'

        self.emailer.send_email(params)


    def send_forgot_password(self, params):

        params['subject'] = "forgot password."
        params['template'] = 'forgot_password'

        self.emailer.send_email(params)