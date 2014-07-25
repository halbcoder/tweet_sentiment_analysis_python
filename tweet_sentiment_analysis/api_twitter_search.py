from TwitterSearch import *

class ApiTwitterSearch:
  
  CONSUMER_KEY = "paJP7dSVwHFwtQb6d8VOWk4qO"
  CONSUMER_SECRET = "eQ5aUrFhOwEfO8QPq0dZmi6AyS1awqEFp2SjE19i08rBvZX160"
  ACCESS_TOKEN = "2566411526-Ul7McFY9oHRRwWXgfTycOeuBdmIM0KbgwUKfiiY"
  ACCESS_TOKEN_SECRET = "bqAetskuhQ398Gru0PuUYV4C2zPgeF8tFNgx47Js9wYCl"

  def authorize(self):
  	return TwitterSearch(
        consumer_key = self.CONSUMER_KEY,
        consumer_secret = self.CONSUMER_SECRET,
        access_token = self.ACCESS_TOKEN,
        access_token_secret = self.ACCESS_TOKEN_SECRET
     )
  	
  def search(self, next_max_id, text = "#F1 -RT"):
    next_max_id = int(next_max_id)

    tso = TwitterSearchOrder()
    tso.setKeywords([text])
    tso.setCount(100)
    # To get the next 100 older than the previous one's last tweet
    if next_max_id != 1:
      tso.setMaxID(next_max_id-1)

    return self.authorize().searchTweets(tso)

