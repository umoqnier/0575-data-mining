import os
import json
from pymongo import MongoClient


def get_db():
    cliente = MongoClient()
    db = cliente["violencia-politica"]
    return db


def get_users():
    with open("usuarias.txt") as f:
        data = f.read().splitlines()
    return data


def get_roles():
    return {"senadoras": "Senadoras", "diputadas": "Diputadas", "senadoras_rep": "Senadoras por Representación",
            "diputadas_rep": "Diputadas por Representación", "candidatas_cdmx": "Candidatas CDMX",
            "candidatas_queretaro": "Candidatas Querétaro", "candidatas_sonora": "Candidatas Sonora"}


def get_tweets_periodo(periodo):
    db = get_db()
    return db.tweets.find({"periodo": periodo})


def tweets_usuaria(path, username):
    """
    This function gets a path and return data frame with tweets and replies information
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
