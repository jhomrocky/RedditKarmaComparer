"""
This application will take the 2 inputs from a user, both being www.reddit.com usernames. Then, it compares
the karma for each of the user's most recent post using the JSON attributes attached to their username, then
notifies the user of who's post got a higher score.
"""

# importing modules
import json
from urllib.request import urlopen

# allows user to pick 2 usernames to compare
# user_one = input("Name: ")
# user_two = input("Name: ")
# user_one = user_one.lower()
# user_two = user_two.lower()

# inserts the two users into 2 variables that uses %s to fill in the username portion
first_json = ("https://www.reddit.com/user/normalism.json") # % user_one)
second_json = ("https://www.reddit.com/user/clockwork8.json") # % user_two)

# loading all data into json representation
first_user_info = json.load(urlopen(first_json))
# grabbing 'data' dictionary key
first_user_info_data = first_user_info['data']
# going deeper, grabbing 'children' key from data dict
first_user_info_children = first_user_info_data['children']
# even further, grabbing the first (most recent post) index from 'children'
first_user_children_data = first_user_info_children[0]
# finally grabbing the text of the message
first_user_post_body = first_user_children_data['data']['body']
# and grabbing the karma score as well
first_user_post_score = first_user_children_data['data']['score']


second_user_info = json.load(urlopen(second_json))
second_user_info_data = second_user_info['data']
second_user_info_children = second_user_info_data['children']
second_user_children_data = second_user_info_children[0]
second_user_post_body = second_user_children_data['data']['body']
second_user_post_score = second_user_children_data['data']['score']

print(first_user_post_body)
print(first_user_post_score)

print(second_user_post_body)
print(second_user_post_score)

