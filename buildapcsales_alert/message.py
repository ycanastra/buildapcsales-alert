def createBody(productName, post, subreddit='buildapcsales'):
	url = post.url.encode('ascii', 'ignore')
	redditUrl = post.permalink.encode('ascii', 'ignore')

	body = ('Hello,\nA post with the keyword "' + productName + '" has been found on ' +
			subreddit + '\n\nHere is the link!\n\n' + url+'\n\n\nHere is the link for ' +
			'the reddit thread!\n\n' + redditUrl)

	unsubscribe = 'If you would like to unsubscribe, please click here.'

	retval = body + '\n\n' + unsubscribe

	return retval

def createSubject(productName, post, subreddit='buildapcsales'):
	subject = '"' + productName + '" found on /r/' + subreddit

	return subject
