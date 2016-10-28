__author__ = 'Leo'
import pymongo
from pymongo import MongoClient
from app.forms import QuizForm

client = MongoClient('localhost', 5000)
db = client['answer-database']

db.