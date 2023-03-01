from flask import Flask, render_template, jsonify

app = Flask(__name__)


JOBS = [
    {'id': 1,
     'title': 'data analyst',
     'location': 'bengaluru India',
     'salary': '$400, 000'},

     {'id': 2,
     'title': 'backend web developer',
     'location': 'Florida',
     'salary': '$300, 000'},
     {'id': 3,
     'title': 'software engineer',
     'location': 'north Carolina',
     'salary': '$500, 000'},
     {'id': 4,
     'title': 'Software Developer',
     'location': 'HP headquarters',
     'salary': '$600, 000'}
]


@app.route("/")
def hello_world():
    return render_template('index.html', jobs=JOBS, company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)