from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC741ffc69c1685f9cca9463023b9bbef4'
auth_token = '8baaedf946572ae1db351708b4a301a2'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+1xxxx',
                     to='++1xxxx'
                 )

print(message.sid)