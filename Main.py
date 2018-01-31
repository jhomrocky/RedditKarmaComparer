"""
This application will take the 2 inputs from a user, both being www.reddit.com usernames. Then, it compares
the karma for each of the user's most recent post using the JSON attributes attached to their username, then
notifies the user of who's post got a higher score.
"""

# importing modules
import json
from urllib.request import urlopen

# allows user to pick 2 usernames to compare
user_one = input("")
user_two = input("")
user_one = user_one.lower()
user_two = user_two.lower()

# inserts the two users into 2 variables that uses %s to fill in the username portion
first_json = ("https://www.reddit.com/user/%s.json" % user_one)
second_json = ("https://www.reddit.com/user/%s.json" % user_two)

# dumping data into json representation
first_user_info = json.load(urlopen(first_json))
second_user_info = json.load(urlopen(second_json))

print(first_user_info)
print(second_user_info)
