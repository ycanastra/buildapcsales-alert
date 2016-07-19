import MySQLdb
import json

def connectToDb():
	f = open('/var/www/run/buildapcsales-alert/credentials.json', 'r')
	cred = json.load(f)
	f.close()

	host = 'localhost'
	user = cred['MYSQL_USER']
	password = cred['MYSQL_PASSWORD']
	database = 'buildapcsales'

	db = MySQLdb.connect(host, user, password, database)

	return db

def getAllProductNames():
	db = connectToDb()
	cursor = db.cursor()

	# execute SQL query using execute() method.
	cursor.execute('USE buildapcsales;')
	cursor.execute('SELECT name FROM Products;')

	# Fetch a single row using fetchone() method.
	data = cursor.fetchall()

	productNames = set([])

	for item in data:
		productNames.add(item[0])

	# disconnect from server
	db.close()

	return productNames

def getUserIdsByProductName(productName):
	db = connectToDb()
	cursor = db.cursor()

	# execute SQL query using execute() method.
	cursor.execute('USE buildapcsales;')
	cursor.execute('SELECT userID FROM Products WHERE name = \"' + productName + '\" ;')

	# Fetch a single row using fetchone() method.
	data = cursor.fetchall()

	userIds = set([])

	for item in data:
		userIds.add(item[0])

	# disconnect from server
	db.close()

	return userIds


def getEmailByUserId(userId):
	db = connectToDb()
	cursor = db.cursor()

	cursor.execute('USE buildapcsales;')
	cursor.execute('SELECT COUNT(1) FROM Users WHERE userID =\"' + userId + '\" ;')

	data = cursor.fetchone()
	count = int(data[0])

	if count == 1:
		cursor.execute('SELECT email FROM Users WHERE userID = \"' + userId + '\" ;')
		data = cursor.fetchone()
		return data[0]

	else:
		return ''
