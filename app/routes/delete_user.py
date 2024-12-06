from flask import Blueprint, request, jsonify
from app.database import get_collection
from app.auth.jwt_required import jwt_required
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('delete_user', __name__)

@bp.route('/delete-user', methods=[''])
@jwt_required
def delete_user():
    pass
