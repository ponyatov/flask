import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/<path>')
def path(path):
    return app.send_static_file(path)

app.run(host='127.0.0.1', port=5000, debug=True)
