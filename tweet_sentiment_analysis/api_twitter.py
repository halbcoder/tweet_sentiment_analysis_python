import twitter

class ApiTwitter:	
	CONSUMER_KEY = "paJP7dSVwHFwtQb6d8VOWk4qO"
	CONSUMER_SECRET = "eQ5aUrFhOwEfO8QPq0dZmi6AyS1awqEFp2SjE19i08rBvZX160"
	ACCESS_TOKEN = "2566411526-Ul7McFY9oHRRwWXgfTycOeuBdmIM0KbgwUKfiiY"
	ACCESS_TOKEN_SECRET = "bqAetskuhQ398Gru0PuUYV4C2zPgeF8tFNgx47Js9wYCl"
	
	def authorize(self):
		return twitter.Api(consumer_key = self.CONSUMER_KEY,
                      consumer_secret = self.CONSUMER_SECRET,
                      access_token_key = self.ACCESS_TOKEN,
                      access_token_secret = self.ACCESS_TOKEN_SECRET)
	
	def fetch_tweet(self, tweet_id):
		return self.authorize().GetStatus(id=tweet_id)

