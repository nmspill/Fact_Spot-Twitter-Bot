import tweepy
import time

CONSUMER_KEY = 'XXXXX'
CONSUMER_SECRET = 'XXXXX'
ACCESS_KEY = 'XXXXX'
ACCESS_SECRET = 'XXXXX'

# authentication of consumer key and secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

# authentication of access token and secret
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def tweet_fact(text_file):
    lines = open(text_file, 'r', errors='ignore').readlines()
    
    for line in reversed(lines):  # traverses through text file of facts
        api.update_status(status=line)  # tweets fact
        print(line, end='')
        del lines[-1]  # deletes the fact off the list
        open(text_file, 'w').writelines(lines)
        time.sleep(60*60)  # time delay (seconds) between tweets

        
 def follow(user_name):
    for follower in tweepy.Cursor(api.followers, screen_name=user_name).items():
        try:
            api.create_friendship(follower.screen_name)
            time.sleep(5)
        except tweepy.TweepError as e:
            print("Sleeping: ", e)
            time.sleep(60*60)



def unfollow():
    for following in tweepy.Cursor(api.friends).items():
        api.destroy_friendship(following.screen_name)
        time.sleep(1)

        
tweet_fact("Facts.txt")
