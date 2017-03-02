from flask import Flask, request, abort,jsonify
from model2 import db
from model2 import User
from model2 import CreateDB
from model2 import app as application
import simplejson as json
from sqlalchemy.exc import IntegrityError
from datetime import datetime
import os

# initate flask app
app = Flask(__name__)

@app.route('/')
def index():
	database = CreateDB(hostname = 'localhost')
	db.create_all()
	return 'CMPE 273 Assignment 1 : Expense management system using Python Flask\n'

# POST /v1/expenses
@app.route('/v1/expenses', methods=['POST'])
def insert_table():
	content = json.loads(request.data)
	if not content or not 'name' in content:
		abort(404)
	database = CreateDB(hostname = 'localhost')
	db.create_all()
	date_strptime = datetime.strptime(content['submit_date'], '%d-%m-%Y')
	user = User(content['id'],content['name'],content['email'],content['category'],
	content['description'],content['link'],content['estimated_costs'],
	date_strptime)
	db.session.add(user)
	db.session.commit()
	user_dict = {
		"id" : user.id,
		"name" : user.name,
		"email" : user.email,
		"category" : user.category,
		"description" : user.description,
		"link" : user.link,
		"estimated_costs" : user.estimated_costs,
		"submit_date" : user.submit_date.strftime('%d-%m-%Y'),
		"status" : user.status,
		"decision_date" : user.decision_date.strftime('%d-%m-%Y')
	}
	return json.dumps(user_dict), 201

# GET /v1/expenses/{expense_id}
@app.route('/v1/expenses/<expense_id>', methods=['GET'])
def get_info(expense_id):
	users = User.query.all()
	users_dict = {}
	for user in users:
		if user.id == int(expense_id):
			users_dict = {
				"id" : user.id,
				"name" : user.name,
				"email" : user.email,
				"category" : user.category,
				"description" : user.description,
				"link" : user.link,
				"estimated_costs" : user.estimated_costs,
				"submit_date" : user.submit_date.strftime('%d-%m-%Y'),
				"status" : user.status,
				"decision_date" : user.decision_date.strftime('%d-%m-%Y')
			}
			break;
	if bool(users_dict):
		return json.dumps(users_dict), 200
	return "User id not found!", 404

# PUT /v1/expenses/{expense_id}
@app.route('/v1/expenses/<id>', methods=['PUT'])
def update_info(id):
	content = json.loads(request.data)
	user = User.query.get(id)
	user.estimated_costs = content['estimated_costs']
	return "success update", 202

# DELETE /v1/expenses/{expense_id}
@app.route('/v1/expenses/<id>', methods=['DELETE'])
def remove_info(id):
	db.session.delete(User.query.get(id))
	db.session.commit()
	return "success delete", 204

# run app service
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5002, debug=True)
