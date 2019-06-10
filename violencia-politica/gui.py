from flask import Flask, render_template
import utils


app = Flask(__name__)


@app.route("/")
def index():
    roles = utils.get_roles()
    usuarias = utils.get_users()
    return render_template("index.html", roles=roles, usuarias=usuarias)


@app.route("/periodo/<periodo>")
def tweets_periodo(periodo):
    data = utils.get_tweets_periodo(periodo)
    return render_template("tweets.html", data=data)


if __name__ == '__main__':
    app.run(debug=True)
