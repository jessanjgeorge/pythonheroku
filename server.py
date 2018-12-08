from bottle import Bottle, run, route, static_file, request, response, template
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
import json
import pymongo
import requests
import time

app = Bottle(__name__)

@app.hook('after_request')
def enable_cors():
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
	response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
	response.headers['Connection'] = 'keep-alive'

@app.route('/')
def root():
	return {'data': 'this is a test heroku server'}
