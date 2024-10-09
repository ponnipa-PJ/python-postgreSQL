from flask import Blueprint, jsonify, request
from app.models.userModel import User
from app import db

bp = Blueprint('user_view', __name__)

@bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{ 'id': user.id, 'name': user.name, 'birthDate': user.birthDate.strftime('%Y-%m-%d'), 'age': user.age } for user in users])

@bp.route('/users/<int:userId>', methods=['GET'])
def get_user(userId):
    user = User.query.get(userId)
    if not user: 
        return jsonify({'error': 'User not found'}), 404  # ส่ง JSON response พร้อมสถานะ 404

    return jsonify({ 'id': user.id, 'name': user.name, 'birthDate': user.birthDate.strftime('%Y-%m-%d'), 'age': user.age }), 200

@bp.route('/users', methods=['POST'])
def add_user():
    data = request.json
    new_user = User(name=data['name'], birthDate=data['birthDate'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({ 'id': new_user.id }), 201

@bp.route('/users/<int:userId>', methods=['PUT'])
def update_user(userId):
    user = User.query.get(userId)
    
    if not user: 
        return jsonify({'error': 'User not found'}), 404 

    data = request.json
    if 'name' in data:
        user.name = data['name']
    if 'birthDate' in data:
        user.birthDate = data['birthDate']
    
    db.session.commit()
    return jsonify({ 'id': user.id, 'name': user.name, 'birthDate': user.birthDate.strftime('%Y-%m-%d'), 'age': user.age }), 200

@bp.route('/users/<int:userId>', methods=['DELETE'])
def delete_user(userId):
    user = User.query.get(userId) 
    if not user:
        return jsonify({'error': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'User deleted successfully'}), 200