from pymongo import MongoClient
from utils import tweets_usuaria, get_users


def main():
    cliente = MongoClient()  # Necesitas tener mongo instalado localmente
    db = cliente["violencia-politica"]
    usuarias = get_users()
    for usuaria in usuarias:
        data = tweets_usuaria("neotweets/", usuaria)
        db.tweets.insert_many(data)


if __name__ == '__main__':
    main()
