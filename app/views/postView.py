from flask import Blueprint, jsonify, request
from app.models.postModel import Post
from app import db

bp = Blueprint('post_view', __name__)

@bp.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([{ 'id': post.id, 'userId': post.userId, 'title': post.title, 'content': post.content, 'createdAt': post.createdAt } for post in posts])

@bp.route('/posts', methods=['POST'])
def add_post():
    data = request.data
    try:
        data = request.get_json(force=True) 
    except UnicodeDecodeError as e:
        return jsonify({"error": "Unable to decode JSON data as UTF-8"}), 400

    new_post = Post(userId=data['userId'], title=data['title'], content=data['content'])
    db.session.add(new_post)
    db.session.commit()
    return jsonify({ 'id': new_post.id }), 201

@bp.route('/posts/<int:postId>', methods=['PUT'])
def update_post(postId):
    post = Post.query.get_or_404(postId)
    
    data = request.json
    if 'title' in data:
        post.title = data['title']
    if 'content' in data:
        post.content = data['content']
    
    db.session.commit()
    return jsonify({ 'id': post.id, 'userId': post.userId, 'title': post.title, 'content': post.content }), 200

@bp.route('/posts/<int:postId>', methods=['DELETE'])
def delete_post(postId):
    post = Post.query.get(postId) 
    if not post:
        return jsonify({'error': 'Post not found'}), 404

    db.session.delete(post) 
    db.session.commit()

    return jsonify({'message': 'Post deleted successfully'}), 200