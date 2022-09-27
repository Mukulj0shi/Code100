from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC741ffc69c1685f9cca9463023b9bbef4'
auth_token = 'd5bc451e2cdea78f3c577c52ba810ff5'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+12545874434',
                     to='+917406663338'
                 )

print(message.sid)