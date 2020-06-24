import tweepy
import sys

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")

consumer_key= input("Input consumer key: ")
consumer_secret=input("Input consumer secret key: ")

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")

access_token= input("Input access token: ")
access_token_secret= input("Input access token secret: ")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
print("Welcome, " + api.me().name + " (" + api.me().screen_name + ")")

# check if user exists
user_exist = True
while user_exist:
    try:
        u = input("Input user's screen name: ")
        user = api.get_user(u)
        print("User found")
        user_exist = False
        break
    except:
        print("User does not exist")
        continue

# checks is user has lists and displays the number if so
# otherwise, quits program
user_list = api.lists_all(user.screen_name)
length = len(user_list)
if length == 1:
    print("This user has 1 list:")
elif length == 0:
    print("This user does not have any lists. Exiting program.")
    sys.exit()
else:
    print("This user has " + str(length) + " lists:")

# displays all lists from user
count = 1
for x in user_list:
    print("{}: {}".format(count, x.name))
    count += 1

# make list seleciton (does not yet account for if list number is invalid)
cur_list = input("Which list would you like to view? (Enter the list number): ")
selection = user_list[int(cur_list) - 1].id

# prints recently followed user upon successful follow
# if user is already being followed, continues program
print("Following all members in the list: ")
members = api.list_members(list_id = selection, slug = user.screen_name)
for scrn_nm in members:
    try:
        api.create_friendship(scrn_nm.screen_name)
        print(scrn_nm.screen_name)
        continue
    except:
        print("Already following this user")
        continue