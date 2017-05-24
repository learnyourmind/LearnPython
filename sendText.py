from twilio import rest
# Account info
account_sid = "AC677fce4641ba82bb8612fc6e78cf3822"
auth_token = "02dde99b2891cff3aeabcc62141da25d"
client = rest.TwilioHttpClient

message = client.sms.message.create(
	body="This is actual message",
	to="+16148592299",
	from_="6148592299")
print message.sid