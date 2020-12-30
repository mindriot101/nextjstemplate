from flask import Flask

app = Flask(__name__)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def foobar(path):
    return {"something": "foobar", "path": path}
