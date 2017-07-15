import json
from twython import Twython
import csv


with open('training_dataset.csv','a') as f:  #change filename accordingly
	writer = csv.writer(f)
	writer.writerow(['tweetID', 'followers', 'listed', 'followings', 'verified', 'Total_favourite_count', 'tweet_favorite_count' ])



with open('test_dataset.csv','a') as f:  #change filename accordingly
	writer = csv.writer(f)
	writer.writerow(['tweetID', 'followers', 'listed', 'followings', 'verified', 'Total_favourite_count', 'tweet_favorite_count'])



api_key = {
	'api_key': 'oKH4zvUKKFuhAlcMUFYdCBzBP',
	'api_secret': 'stpAIR08KG4k5a8vx1bUbsPrZzgiE9908N2zWe0e9AUDpSsAC7',
	'access_token': '30828296-lG2ARxNicDrZGVMtKj4nsc5KtkzXMoSdnAUicU9pi',
	'access_token_secret': 'XPZDCQtecjSA0qnMl4M06B5qB92FeJ1MMHho9ZFj51fCd'
}

twitter= Twython(api_key['api_key'],
				api_key['api_secret'],
				api_key['access_token'],
				api_key['access_token_secret']
				)

maxTweets = 10000
tweetCount = 0

# ID of the most recent tweet
max_id = -1

count = 0

while tweetCount < maxTweets:
	list_of_tweets = []

	if (max_id <= 0):
		new_statuses = twitter.search(q='modi', count="100", include_entities= True)
		print(1)

	else:
		new_statuses = twitter.search(q='modi', count="100", include_entities = True, max_id=max_id - 1)
		print(3)

	tweetCount += len(new_statuses['statuses'])

	print tweetCount

	for tweet in new_statuses['statuses']:
		count += 1
		post = tweet
		list_of_tweets.append(post['id'])

		post['_id'] = post['id']

		Text = post['text'].encode('utf8')
		followers = post['user']['followers_count']
		followings = post['user']['friends_count']
		fav_count = post['user']['favourites_count']  #total favourites
		listed = post['user']['listed_count']
		favorite_count = post['favorite_count']  #favourites received

		# print post['user']['verified']

		if post['user']['verified'] == False:
			ver = 0
		else:
			ver = 1


		username = post['user']['screen_name']



		if count >= 5000:

			with open('new2_test_dataset.csv','a') as f:  #change filename accordingly
				writer = csv.writer(f)
				writer.writerow([post['id'], int(followers), int(listed), int(followings), int(ver), int(fav_count), int(favorite_count) ])

		else:

			with open('new2_training_dataset.csv','a') as f:  #change filename accordingly
				writer = csv.writer(f)
				writer.writerow([post['id'], int(followers), int(listed), int(followings), int(ver), int(fav_count), int(favorite_count) ])

	max_id = sorted(list_of_tweets)[0]

	# print tc

print "Total tweets: ", tweetCount

