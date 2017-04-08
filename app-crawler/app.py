from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('results.html', name="App 1")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
