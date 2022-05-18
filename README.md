# [@ferdie_bot](https://twitter.com/ferdie_bot)
A bot that consumes the [Twitter API](https://github.com/bear/python-twitter) and retweets all incoming public tweets containing the phrase “I am Ferdinand von Aegir” (popular [meme](https://knowyourmeme.com/memes/i-am-ferdinand-von-aegir) from Nintendo’s Fire Emblem Franchise).
Currently deployed on AWS using Lambda Functions. 

Wanna see if it works? Go on your Twitter account and tweet something containing the phrase “I am Ferdinand von Aegir” and wait til you get retweeted!

## Try it yourself
You can create your own twitter retweet bot by providing the necessary data through environment variables.
### Pre-requisites
- [A Twitter Developer Account](https://developer.twitter.com/en)
- [An AWS Account](https://aws.amazon.com/) (Free-tier is good enough)
### Setup
1. Create a deployment `package` with the Twitter dependency
```    
pip install --target ./package python-twitter
```

2. Copy the `lambda_function.py` file into the newly created `package`
3. Zip the `package` file
4. Create a new AWS Lambda Function and upload the .zip file from above
5. Create the following environment variables with your own values

| Key                     | Value                                             |
|-------------------------|---------------------------------------------------|
| ACCESS_TOKEN_KEY        | Twitter Developer Account Credentials           |
| ACCESS_TOKEN_SECRET     | Twitter Developer Account Credentials           |
| IS_ACTIVE               | True or False                                   |
| CONSUMER_KEY            | Twitter Developer Account Credentials           |
| CONSUMER_SECRET         | Twitter Developer Account Credentials           |
| PHRASES                 | Phrases to retweet (String separated by commas) |
| RETRIEVAL_INTERVAL_MINS | Integer                                         |

6. After you've deployed the code, you have to create an Amazon EventBridge rule and set the target as the Lambda function you just created
7. Set the event schedule to be the same value as RETRIEVAL_INTERVAL_MINS
8. That's it! Test your bot by tweeting one of your magic phrases
