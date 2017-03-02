import sqlalchemy
from sqlalchemy import Column, Integer, DateTime, String, Float
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

app = Flask(__name__)

# Database Configurations
DATABASE = 'mysqldb'
PASSWORD = 'root123'
USER = 'root'
HOSTNAME = 'localhost'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s/%s'%(USER, PASSWORD, HOSTNAME, DATABASE)
db = SQLAlchemy(app)

# Database migration command line
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), unique = False)
	email = db.Column(db.String(120), unique = False)
	category = db.Column(db.String(80), unique = False)
	description = db.Column(db.String(120), unique = False)
	link = db.Column(db.String(120), unique = False)
	estimated_costs = db.Column(db.Float, unique = False)
	submit_date = db.Column(db.DateTime, unique = False)
	status = db.Column(db.String(80), unique = False)
	decision_date = db.Column(db.DateTime, unique = False)

	def __init__(self,id,name,email,category,description,link,estimated_costs,submit_date):
		# initialize columns
		self.id = id
		self.name = name
		self.email = email
		self.category = category
		self.description = description
		self.link = link
		self.estimated_costs = estimated_costs
		self.submit_date = submit_date
		self.status = "pending"
		self.decision_date = submit_date

	def __repr__(self):
		return '<User %r>' % self.name

class CreateDB():
	def __init__(self, hostname=None):
		if hostname != None:
			HOSTNAME = hostname
		engine = sqlalchemy.create_engine('mysql://%s:%s@%s'%(USER, PASSWORD, HOSTNAME)) # connect to server
		engine.execute("CREATE DATABASE IF NOT EXISTS %s "%(DATABASE)) #create db

if __name__ == '__main__':
	manager.run()
