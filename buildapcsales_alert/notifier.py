import reddit
import mysql
import message
import gmail

import httplib2
from apiclient import discovery

credentials = gmail.get_credentials()
http = credentials.authorize(httplib2.Http())
service = discovery.build('gmail', 'v1', http=http)

posts = reddit.getNewPosts()

productNames = mysql.getAllProductNames()

stuff = []

for item in posts:
	title = item.title.encode('ascii', 'ignore')
	for item2 in productNames:
		if item2 in title:
			userIDs = mysql.getUserIdsByProductName(item2)

			for item3 in userIDs:
				stuff.append((item3, item2, item))



for item in stuff:
	userId = item[0]
	productName = item[1]
	post = item[2]

	subject = message.createSubject(productName, post)
	body = message.createBody(productName, post)
	recipient = mysql.getEmailByUserId(userId)

	if len(recipient) == 0:
		continue

	messageToSend = gmail.createMessage('sales.bot.noreply@gmail.com',
								  recipient,
								  subject,
								  body)

	gmail.sendMessage(service, 'sales.bot.noreply@gmail.com', messageToSend)
