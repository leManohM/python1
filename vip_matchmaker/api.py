from flask import Flask, request, jsonify, render_template
from .matching import match_groups_to_tables
from .utils import calculer_score

app = Flask(__name__)

@app.route("/match", methods=["POST"])
def match_route():
    payload = request.get_json()
    groupes = payload.get("groupes", [])
    tables = payload.get("tables", [])
    matches = match_groups_to_tables(groupes, tables)
    return jsonify({"matches": [{"groupe": g, "table": t} for g, t in matches]})

@app.route("/score", methods=["POST"])
def score_route():
    g = request.get_json()
    score = calculer_score(g)
    return jsonify({"score": score})

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
