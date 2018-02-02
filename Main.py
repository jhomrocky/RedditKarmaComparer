"""
This application will take the 2 inputs from a user, both being www.reddit.com usernames. Then, it compares
the karma for each of the user's most recent post using the JSON attributes attached to their username, then
notifies the user of who's post got a higher score.
"""

# importing modules
import sys
import json
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from time import sleep


def check_users():
    # allows user to pick 2 usernames to compare
    user_one = input("Name: ")

    # uses input to put username into url
    first_json_url = ("https://www.reddit.com/user/%s.json" % user_one)

    # requests url, returns error message if a username does not exist, then restarts function if name not found
    first_username_check = Request(first_json_url)
    try:
        urlopen(first_username_check)
    except HTTPError as reason:
        if reason.code == 404:
            print("Incorrect username. Try again.")
            check_users()
        # this elif is here since the error kept popping up in testing)
        elif reason.code == 429:
            print("Too many requests. Try again.")
            check_users()
    # once we know the username is real, we then load into a json object
    first_user_info = json.load(urlopen(first_json_url))

    user_two = input("Name: ")
    second_json_url = ("https://www.reddit.com/user/%s.json" % user_two)
    second_username_check = Request(second_json_url)
    try:
        urlopen(second_username_check)
    except HTTPError as reason:
        if reason.code == 404:
            print("Incorrect username. Try again")
            check_users()
        elif reason.code == 429:
            print("Too many requests. Try again.")
            check_users()
    second_user_info = json.load(urlopen(second_json_url))
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

    # for purposes of explanation I chose to do it this way, it could have been done:
    # first_user_info_data = first_user_info['data']['children'][0]['data']['body']
    # unfortunately, in that form the data is put as a string so the later check
    # of which score is higher fails

    # repeat of above for second user, using shorter syntax
    second_user_post_body = second_user_info['data']['children'][0]['data']['body']
    second_user_post_score = second_user_info['data']['children'][0]['data']['score']

    # prints post body & score for both users
    print("%s\'s post:\n%s\n" % (user_one, first_user_post_body))
    print("%s\'s score:\n%d\n" % (user_one, first_user_post_score))

    print("%s's post:\n%s\n" % (user_two, second_user_post_body))
    print("%s's score:\n%d\n" % (user_two, second_user_post_score))

    # prints different messages based on higher score
    if first_user_post_score > second_user_post_score:
        print("%s did better on their post." % user_one)
    else:
        print("%s did better on their post." % user_one)

    user_retry = input("Do another set of usernames? Y for yes, N for no:\n> ")
    user_retry = user_retry.lower()
    if user_retry == 'y':
        check_users()
    else:
        print("Take care!")
        sleep(2)
        sys.exit()


# starts check
check_users()
