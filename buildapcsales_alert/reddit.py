import praw

from run_time import getLastRunTime
from run_time import updateRunTime

def getNewPosts(subreddit='buildapcsales', limit=40):
	r = praw.Reddit(user_agent='User-Agent: buildapcsales_alertv1.0 (by /u/Sankyuu)')
	submissions = r.get_subreddit(subreddit).get_new(limit=limit)

	newSubmissions = []
	lastRunTime = getLastRunTime()
	# updateRunTime()

	for item in submissions:
		postCreationTime = float(item.created_utc)
		if postCreationTime > lastRunTime:
			newSubmissions.append(item)

	return newSubmissions
