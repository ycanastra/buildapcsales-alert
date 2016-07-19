import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

from email.mime.text import MIMEText
import base64
import urllib2
import argparse


def get_credentials():
	"""Gets valid user credentials from storage.

	If nothing has been stored, or if the stored credentials are invalid,
	the OAuth2 flow is completed to obtain the new credentials.

	Returns:
		Credentials, the obtained credential.
	"""

	try:
		flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
	except ImportError:
		flags = None

	# If modifying these scopes, delete your previously saved credentials
	# at ~/.credentials/gmail-python-quickstart.json
	SCOPES = 'https://www.googleapis.com/auth/gmail.send'
	CLIENT_SECRET_FILE = 'client_secret.json'
	APPLICATION_NAME = 'Buildapcsales Alert - Gmail'

	home_dir = os.path.expanduser('~')
	credential_dir = os.path.join(home_dir, '.credentials')

	if not os.path.exists(credential_dir):
		os.makedirs(credential_dir)

	credential_path = os.path.join(credential_dir, 'gmail-buildapcsales_alert.json')

	store = oauth2client.file.Storage(credential_path)
	credentials = store.get()

	if not credentials or credentials.invalid:
		flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
		flow.user_agent = APPLICATION_NAME

		if flags:
			credentials = tools.run_flow(flow, store, flags)

		else: # Needed only for compatibility with Python 2.6
			credentials = tools.run(flow, store)

		print('Storing credentials to ' + credential_path)

	return credentials

def main():
	get_credentials()


def sendMessage(service, user_id, message):
	# try:
	message = (service.users().messages().send(userId=user_id, body=message).execute())
	print('Message Id: ' + message['id'])
	return message
	# except urllib2.HTTPError, error:
	# 	print('An error occurred: ' + error)


if __name__ == '__main__':
	main()
