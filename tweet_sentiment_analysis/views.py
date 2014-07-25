from django.shortcuts import render
from django.http import HttpResponse
import api_twitter_search
import api_twitter
import api_idol
import re



def tweet_list(request, max_id):
	max_id = re.findall(r'\d+', request.path)[0]
	ts_api = api_twitter_search.ApiTwitterSearch()
	response = ts_api.search(next_max_id=max_id)
	print response['content']['search_metadata']
	return render(request, 'tweet_list.html', {'item_list': response})

def tweet_details(request, tweet_id):
	tweet_id = re.findall(r'\d+', request.path)[0]
	
	t_api = api_twitter.ApiTwitter()
	tweet_details = t_api.fetch_tweet(tweet_id)
	tweet_text = tweet_details.text
	
	idol_api = api_idol.ApiIdol()
	language = idol_api.call_api("identifylanguage", tweet_text)
	sentiment = idol_api.call_api("detectsentiment", tweet_text)

	pos_tweet = highlight_tweet(tweet_text, sentiment, "positive")
	neg_tweet = highlight_tweet(tweet_text, sentiment, "negative")

	return render(request, 'tweet_details.html', {'tweet': tweet_details, 
		'language': language.json(), 'sentiment': sentiment.json(), 'pos_tweet': pos_tweet.json(), 
		'neg_tweet': neg_tweet.json()})


def collect_sentiment_terms(item_list):
	terms = []			
	for item in item_list:
		terms.append(item["sentiment"])	
	if terms and terms[0] is None:
		terms = [" "]
	return terms

def highlight_tweet(tweet_text, sentiment, sentiment_type):
	idol_api = api_idol.ApiIdol()
	s = sentiment.json()
	terms = collect_sentiment_terms(s[sentiment_type])
	tweet = idol_api.highlight_text(tweet_text, terms, "<span class={}>".format(sentiment_type))
	return tweet

