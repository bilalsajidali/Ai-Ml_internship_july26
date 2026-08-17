from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/abdullah")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/data")
def api_data():
    return jsonify({
        "title": "Internship Team",
        "members": [
            {"name": "Abdullah", "role": "AI/ML Intern", "tests_done": 4},
            {"name": "Mahad", "role": "AI/ML Intern", "tests_done": 4},
            {"name": "Zarmeen", "role": "AI/ML Intern", "tests_done": 4},
            {"name": "Zeeshan", "role": "AI/ML Intern", "tests_done": 6},
        ],
    })


if __name__ == "__main__":
    app.run(debug=True)
