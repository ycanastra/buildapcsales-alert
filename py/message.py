from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import base64

def createBody(productName, post, subreddit='buildapcsales'):
	# url = post.url.encode('ascii', 'ignore')
	# redditUrl = post.permalink.encode('ascii', 'ignore')
	#
	# body = ('Hello,\nA post with the keyword "' + productName + '" has been found on ' +
	# 		subreddit + '\n\nHere is the link!\n\n' + url+'\n\n\nHere is the link for ' +
	# 		'the reddit thread!\n\n' + redditUrl)
	#
	# return body

	msg = MIMEMultipart('alternative')
	msg['to'] = to
	msg['from'] = sender
	msg['subject'] = subject

def createSubject(productName, post, subreddit='buildapcsales'):
	subject = '"' + productName + '" found on /r/' + subreddit

	return subject

def createUnsubLinks(productName, userid):
	unsubscribe = 'If you would like to unsubscribe, please click '

	unsubEmailLink = 'http://159.203.229.225/chrome_extension_files/unsubscribe_keyword.php?userid=' + userid + '&keyword=' + productName

	unsubscribeEmailLink = '<a href=\"' + unsubEmailLink + '\">here</a>'

	return unsubscribe + unsubscribeEmailLink

def createMessage(productName, userId, post, recipient, subreddit='buildapcsales'):
	msg = MIMEMultipart('alternative')
	msg['to'] = recipient
	msg['from'] = 'sales.bot.noreply@gmail.com'
	msg['subject'] = post.title #createSubject(productName, post)

	postPermalink = post.permalink
	postUrl = post.url

	unsubKeywordlLink = 'http://159.203.229.225/buildapcsales-alert/php/unsubscribe_keyword.php?userid=' + userId + '&keyword=' + productName
	unsubEmailLink = 'http://159.203.229.225/buildapcsales-alert/php/unsubscribe_email.php?userid=' + userId + '&email=' + recipient

	body = """
		<html>
		  <head></head>
		  <body>
		    <p>
				Hello!
				<br>
				<br>
				A post with the keyword {0} has been found on {1}!
				<br>
				<br>
				<a href="{2}">Click here</a> to go to directly to the link!
				<br>
				<a href="{3}">Click here</a> to go to the reddit permalink!
				<br>
				<br>
				If you would like to unsubscribe your email from further buildapcsales
				alert emails, please <a href="{4}">click here</a>
				<br>
				If you would like to unsubscribe from the keyword {0} then please
				<a href="{5}">click here</a>
				<br>
				<br>
				Thank you!
		    </p>
		  </body>
		</html>
		"""

	newBody = body.format(productName, subreddit, postUrl, postPermalink, unsubEmailLink, unsubKeywordlLink)

	msg.attach(MIMEText(newBody, 'html'))

	return {'raw': base64.urlsafe_b64encode(msg.as_string())}
