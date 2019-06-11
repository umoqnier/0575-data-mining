from pymongo import MongoClient


def get_db():
    cliente = MongoClient()
    db = cliente["violencia-politica"]
    return db


def get_usuarias_rol(rol):
    db = get_db()
    return db.tweets.distinct("usuaria", {"rol": rol})


def get_usuarias_periodo(periodo):
    db = get_db()
    return db.tweets.distinct("usuaria", {"periodo": periodo})


def get_tweets(username):
    db = get_db()
    return db.tweets.find({"usuaria": username})


def get_tweet(tweet_id):
    db = get_db()
    return db.tweets.find({"_id": tweet_id})


def get_replies(username, tweet_id):
    db = get_db()
    return db.tweets.find({"usuaria": username, "_id": tweet_id})
