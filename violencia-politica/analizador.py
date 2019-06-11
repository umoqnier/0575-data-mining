from pymongo import MongoClient
from textblob import TextBlob
import textblob

def analizador(text):
    analizer = TextBlob(text)
    try:
        texto_traducido = analizer.translate(to="en")  # para el uso del paquete de analisis sentimental se requiere texto en ingles
    except textblob.exceptions.NotTranslated:
        print("[ERROR] No se pudo traducir", text)
        return 0.0
    return texto_traducido.sentiment.polarity