from flask import Flask, render_template
import utils
import queries
from analizador import analizador

app = Flask(__name__)


@app.route("/")
def index():
    roles = utils.get_roles()
    usuarias = utils.get_users()
    return render_template("index.html", roles=roles, usuarias=usuarias)


@app.route("/periodos/<periodo>")
def tweets_periodo(periodo):
    data = list(queries.get_usuarias_periodo(periodo))
    return render_template("usuarias_periodo.html", data=data)


@app.route("/roles/<rol>")
def usuarias_rol(rol):
    data = list(queries.get_usuarias_rol(rol))
    roles = utils.get_roles()
    return render_template("usuarias_rol.html", candidatas=data,
                           rol_display=roles[rol])


@app.route("/usuaria/<username>")
def usuaria(username):
    data = list(queries.get_tweets(username))
    detalles = utils.get_perfil_usuaria(username)
    detalles.profile_image_url = detalles.profile_image_url[:-1 * len("_normal.jpg")] + "_400x400.jpg"
    return render_template("tweets.html", tweets=data, usuaria=username, info=detalles)


@app.route("/usuaria/<username>/replies/<tweet_id>/")
def replies(username, tweet_id):
    data = list(queries.get_replies(username, tweet_id)).pop()
    replies = data["replies"]
    for r in replies:
        r["polaridad"] = analizador(r["text"])
    return render_template("replies.html", replies=replies, usuaria=username, tweet=data["tweet"])


if __name__ == '__main__':
    app.run(debug=True)
