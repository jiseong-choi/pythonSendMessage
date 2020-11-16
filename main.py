# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC74983c722cf98d6ad147fb1cdc8e4980'
auth_token = 'd8fa0314347c81c4ae6201cd829572cb'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="안녕하세요 반가워요^^ \n",
                     from_='+12037174446',
                     to='+82 1086601154'
                 )

print(message.sid)