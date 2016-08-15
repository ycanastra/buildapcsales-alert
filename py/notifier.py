import reddit
import mysql
import message
import gmail

import smtplib

import httplib2
from apiclient import discovery

def normalize(productName):
	return productName.replace(' ', '')

def permutate(productName):
	return productName.replace(' ', '-')

def main():
	# credentials = gmail.get_credentials()
	# http = credentials.authorize(httplib2.Http())
	# service = discovery.build('gmail', 'v1', http=http)

	posts = reddit.getNewPosts()

	productNames = mysql.getAllProductNames()

	stuff = []

	for item in posts:
		title = item.title.encode('ascii', 'ignore')
		for item2 in productNames:
			keywordList = set([item2, normalize(item2), permutate(item2)])
			if any(x.lower() in title.lower() for x in keywordList):
				userIDs = mysql.getUserIdsByProductName(item2)

				for item3 in userIDs:
					stuff.append((item3, item2, item))



	for item in stuff:
		userId = item[0]
		productName = item[1]
		post = item[2]

		subject = message.createSubject(productName, post)
		# body = message.createBody(productName, post)
		# unsubscribeLinks = message.createUnsubLinks(productName, userId)
		recipient = mysql.getEmailByUserId(userId)

		if len(recipient) == 0:
			continue

		msg = message.createMessage(productName, userId, post, recipient)

		try:
			s = smtplib.SMTP('localhost')
			s.sendmail('noreply@buildapcsales-alert.com', [recipient], msg.as_string())
			print 'message sent!'
		except:
			print 'An error occurred'

		# try:
		# 	gmail.sendMessage(service, 'sales.bot.noreply@gmail.com', msg)
		# except:
		# 	print 'An error occurred'

if __name__ == "__main__":
	main()
