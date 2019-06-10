from pymongo import MongoClient
from textblob import TextBlob


def analizador_replies():
    usuaria = "@delfinagomeza"
    cliente = MongoClient()
    db = cliente["violencia-politica"]
    tweets = db.tweets.find({"usuaria": usuaria})
    total_tweets = db.tweets.count_documents({"usuaria": usuaria})
    for tweet in tweets:
        for i, reply in enumerate(tweet["replies"]):
            analizer = TextBlob(reply["text"])
            texto_traducido = analizer.translate(to="en")  # para el uso del paquete de analisis sentimental se requiere texto en ingles
            reply["polaridad"] = texto_traducido.sentiment.polarity
            print("Respuesta: '", reply["text"], "'")
            if reply["polaridad"] < 0.0:
                print("La respuesta es NEGATIVA")
            elif reply["polaridad"] > 0.0:
                print("La respuesta es POSITIVA")
            else:
                print("La respuesta es NEUTRAL")
