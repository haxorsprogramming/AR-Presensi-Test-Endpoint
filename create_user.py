from flask import Flask, jsonify, request

app = Flask(__name__)

data_user = [
  { 'usernam': 'admin', 'password': 'admin', 'email' : 'admin@gmail.com' }
]


@app.route("/")
def hello_world():
  return "AR REST API!!!, Keep Smile"


@app.route('/data_user')
def get_user():
  return jsonify(incomes)
