from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        "place": "Bangalore",
        "Title": "Data analyst"
    },

    {
        'id': 2,
        "place": "Chennai",
        "Title": "Data Scientist"
    },

    {
        'id': 3,
        "place": "Mumbai",
        "Title": "Web developer"
    }
]


@app.route("/")
def hello_jovian():
    return render_template('index.html', jobs = JOBS)

if __name__ == "__main__":
    app.run(debug=True)