import re
from flask import Flask ,render_template, url_for

app = Flask(__name__)

posts = [

    {
        'Movie_name':'Iron man',
        'Genre':'Action'
    },
    {
        'Movie_name':'Iron man2',
        'Genre':'Action|War|Fiction'
    }
]
@app.route("/")
def home():
    return render_template('home.html',posts=posts)

@app.route("/code")
def code():
    return render_template('code.html')

@app.route("/recommend")
def recommend():
    return render_template('recommend.html')

@app.route("/presentation")
def present():
    return render_template('presentation.html')

@app.route("/member")
def member():
    return render_template('member.html')

if __name__=="__main__":
    app.run(debug=True,port = 8000)