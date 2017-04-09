from flask import Flask, request, render_template, session
from utils.AppStore import AppStore

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    if not session.get("last_search"):
        session["last_search"] = None
    if request.method == 'POST':
        app_name = request.values.get("search")
        appstore = AppStore()
        data = appstore.app_global_ranking(app_name)
        if data:
            session["last_search"] = data
            return render_template('results.html', app=data)
        return render_template('not_on_charts.html')
    else:
        return render_template('search.html', app=session["last_search"])


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.route('/session', methods=["GET", "POST"])
def see_session():
    import ipdb; ipdb.set_trace()
    return "ok"


if __name__ == "__main__":
    app.secret_key = "a45,35DAD.@TL$32b#45snfhi"
    app.run(host='0.0.0.0', debug=True)
