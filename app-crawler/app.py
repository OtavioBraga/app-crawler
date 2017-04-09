from flask import Flask, request, render_template
from utils.AppStore import AppStore

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        app_name = request.values.get("search")
        appstore = AppStore()
        data = appstore.app_global_ranking(app_name)
        if data:
            return render_template('results.html', app=data)
        return render_template('not_on_charts.html')
    else:
        return render_template('search.html')


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
