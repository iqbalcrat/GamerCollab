from flask import Flask, render_template, request, redirect, url_for
import pyrebase



config = {
    'apiKey': 'api_key',
    'authDomain': 'auth_domain',
    'databaseURL': 'database_url',
    'projectId': 'gamercollab-e8a25',
    'storageBucket': 'gamercollab-e8a25.appspot.com',
    'messagingSenderId': '687236169723',
    'appId': 'app_id',
    'measurementId': 'G-YH9314G9ZF'
}

app = Flask(__name__)
firebase = pyrebase.initialize_app(config)
db = firebase.database()


@app.route("/", methods = ["GET", "POST"])
@app.route("/home", methods = ["GET", "POST"])
def home():
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route("/register", methods = ["GET", "POST"])
def register():
    if request.method == "POST":
        email=request.form["email"]
        if email:
            db.child("email").push(email)
            success = "Thanks for you interest in GamerCollab, we will notify you once the beta product is ready."
            return render_template('index.html', success=success)
        else:
            error = "Kinldy enter your email id."
            return render_template("index.html", error=error)
    else:
        return render_template("404.html")

if __name__ == '__main__':
    app.run()
