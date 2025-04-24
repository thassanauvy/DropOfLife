# flaskAPI/auth.py
from flask import Blueprint, request, jsonify

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    return jsonify({"message": "Login successful", "user": data['username']})

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    return jsonify({"message": "Signup successful", "user": data['username']})
