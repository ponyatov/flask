import flask

app = flask.Flask(__name__)

@app.route('/')
def index(): return 'hello'

app.run(host='127.0.0.1', port=12700, debug=True)
