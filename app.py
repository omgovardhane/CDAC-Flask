
import re
from flask import Flask ,render_template, url_for,request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/downdump")
def downdump():
    return render_template('downdump.html')


@app.route('/rate', methods =["GET", "POST"])
def rate():
    if request.method == "POST":
        mov_rating_1 = int(request.form.get("movie1"))
        mov_rating_2 = int(request.form.get("movie2"))
        mov_rating_3 = int(request.form.get("movie3"))
        mov_rating_4 = int(request.form.get("movie4"))
        mov_rating_5 = int(request.form.get("movie5"))
        dit={1193:mov_rating_1,661:mov_rating_2,914:mov_rating_3,3408:mov_rating_4,2355:mov_rating_5}
        import get_user_rating
        get_user_rating.update_rating(dit)
        import recommend
        a =recommend.give_recom()
        return render_template('presentation.html',lms=a)
    return render_template('rate.html')

    

@app.route("/down")
def down():
    import down
    return render_template('done.html')

@app.route("/dump")
def dump():
    import dump_data
    return render_template('done.html')


if __name__=="__main__":
    app.run(debug=True,port = 8080)













