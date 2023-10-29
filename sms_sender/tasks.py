import  os
from celery import shared_task
from twilio.rest import Client


@shared_task
def send_sms(phone_number):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='+16562187892',
        body='Hello from test app🐥',
        to='phone_number'
    )
    print(message.sid)
    return f"SMS надіслано до {phone_number}, SID: {message.sid}"
