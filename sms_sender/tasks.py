import  os
from celery import shared_task
from twilio.rest import Client


@shared_task
def send_sms(phone_number):
    account_sid = 'ACb069a93dfbb09db1f04623247d85be67'
    auth_token = '6f5a85103a12c07eb9996aef5e84da43'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='+16562187892',
        body='Hello from test app🐥',
        to='phone_number'
    )
    print(message.sid)
    return f"SMS надіслано до {phone_number}, SID: {message.sid}"
#'ACb069a93dfbb09db1f04623247d85be67'
#os.environ['TWILIO_ACCOUNT_SID']
#os.environ['TWILIO_AUTH_TOKEN']