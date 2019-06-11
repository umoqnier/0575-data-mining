import os
import json
import tweepy
from tokens import ACCESS_T, ACCESS_TS, CONSUMER_K, CONSUMER_S


def get_twitter_api():
    auth = tweepy.OAuthHandler(CONSUMER_K, CONSUMER_S)
    auth.set_access_token(ACCESS_T, ACCESS_TS)
    api = tweepy.API(auth)
    return api


def get_perfil_usuaria(username):
    api = get_twitter_api()
    data = api.get_user(username)
    return data


def get_users():
    with open("usuarias.txt", 'r') as f:
        data = f.read().splitlines()
    return data


def get_roles():
    return {"senadoras": "Senadoras", "diputadas": "Diputadas",
            "senadoras_rep": "Senadoras por Representación",
            "diputadas_rep": "Diputadas por Representación",
            "candidatas_cdmx": "Candidatas CDMX",
            "candidatas_queretaro": "Candidatas Querétaro",
            "candidatas_sonora": "Candidatas Sonora"}


def tweets_usuaria(path, username):
    """
    This function gets a path and return data frame with tweets
    and replies information
    :param path: String from the base path to search tweets
    :return: Dataframe with json objects, that represent a tweet, as contain
    """
    ids = []
    tweets = []
    with open(path + username + ".json", 'r') as f:
        raw_data = f.readlines()
    for line in raw_data:
        data = json.loads(line)
        if data["_id"] in ids:
            print("[", data["_id"], "]", "Saltando id duplicado de", username)
        else:
            ids.append(data["_id"])
            tweets.append(data)
    return tweets


def get_files_path(search_path, extension=''):
    """
    This function search files from path
    :param search_path: String of start path
    :param extension: Pattern to match in files search
    :return: List of path+file_name
    """
    matches = []
    for path, dirs, files in os.walk(search_path):
        for file in files:
            if extension in file:
                matches.append(os.path.join(path, file))
    return matches
