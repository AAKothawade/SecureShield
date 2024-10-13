

from twilio.rest import Client

# Your Account SID and Auth Token from twilio.com/console
account_sid = 'AC5a99ca7bee197593fb43a67f0e541af8'
auth_token = 'fb495539828707c67eeb125d37d743b4'
client = Client(account_sid, auth_token)

# Making a call
call = client.calls.create(
    twiml='<Response><Say>+919890107615</Say></Response>',
    to='+919890107615',
    from_='+12254604195'
)

print(f"Call SID: {call.sid}")

