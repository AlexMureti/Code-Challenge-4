from flask import Blueprint, jsonify, request
from config import db

api = Blueprint("api", __name__)

@api.route("/")
def home():
    return jsonify({"message": "my phas4 Code Challenge API"})
