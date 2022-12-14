from textblob import TextBlob
import sys
import tweepy
import matplotlib.pyplot as plt


def percentage(part, whole):
    return 100 * float(part) / float(whole)


consumerKey = "API_Key"
consumerSecret = "API_Key_Secret"
Bearer_Token = "Bearer_Token"
AccessToken = "AccessToken"
AccessTokenSecret = "AccessTokenSecret"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(AccessToken, AccessTokenSecret)
api = tweepy.API(auth)

searchTerm = input("Enter keyword to search about: ")
noOfSearchTerms = int(input("Enter how many tweets to analyze: "))

tweets = tweepy.Cursor(api.search_tweets, q=searchTerm, lang="en").items(noOfSearchTerms)

positive = 0
negative = 0
neutral = 0
polarity = 0

i = 1
for tweet in tweets:
    print(str(i) + ') ' + tweet.text + '\n')
    i = i + 1
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity

    if analysis.sentiment.polarity == 0:
        neutral += 1
    elif analysis.sentiment.polarity < 0.00:
        negative += 1
    elif analysis.sentiment.polarity > 0.00:
        positive += 1

positive = percentage(positive, noOfSearchTerms)
negative = percentage(negative, noOfSearchTerms)
neutral = percentage(neutral, noOfSearchTerms)
polarity = percentage(polarity, noOfSearchTerms)

positive = format(positive, '.2f')
negative = format(negative, '.2f')
neutral = format(neutral, '.2f')

print("How people are reacting on " + searchTerm + " by analyzing " + str(noOfSearchTerms) + " Tweets.")
if polarity == 0.00:
    print("Neutral")
elif polarity < 0.00:
    print("Negative")
elif polarity > 0.00:
    print("Positive")

    labels = ['Positive [' + str(positive) + '%]', 'Negative [' + str(negative) + '%]',
              'Neutral [' + str(neutral) + '%]']
    sizes = [positive, negative, neutral]
    colors = ['red', 'blue', 'yellow']
    patches, texts = plt.pie(sizes, colors=colors, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.title("How people are reacting on " + searchTerm + " by analyzing " + str(noOfSearchTerms) + " Tweets.")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
