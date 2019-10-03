import json
import requests
import xml.etree.ElementTree as ET
"""
`FROM` Account details
"""
from_acct_userid = "xxxx"
from_acct_userkey = "xxxx"
from_acct_usersecret = "xxxx"

"""
`TO` Account details
"""

to_acct_userid = "xxxx"
to_acct_userkey = "xxxx"
to_acct_usersecret = "xxxx"


"""
Populate book ids from the shelves list
API Endpoint: 	https://www.goodreads.com/review/list/{{amz_userid}}.xml?\
				key={{amz_userkey}}&v=2&shelf=to-read&per_page=200&page=1
"""
def populate_book_ids(shelves_list):
	shelf_to_books = {}
	for shelf in shelves_list:
		shelf_to_books[shelf] = []
		endpoint_url = "https://www.goodreads.com/review/list/{0}.xml?key={1}&v=2&shelf={2}&per_page=200&page=1".format(from_acct_userid,from_acct_userkey,shelf)
		response = requests.get(endpoint_url).text
		root = ET.fromstring(response)
		for child in root:
			print child.tag, child.attrib
		break	



"""
Populate shelves list from the first account
API Endpoint: https://www.goodreads.com/shelf/list.json?key={{amz_userkey}}
"""
def get_shelves_list():
	shelves_list = []
	endpoint_url = "https://www.goodreads.com/shelf/list.json?key={}".format(from_acct_userkey)
	response = json.loads(requests.get(endpoint_url).text)
	shelves_obj_list = response['shelves']['user_shelves']
	for shelf in shelves_obj_list:
		shelves_list.append(shelf['name'])
	return shelves_list



def main():
	shelves_list = get_shelves_list()
	populate_book_ids(shelves_list)
	print(shelves_list)


main()	