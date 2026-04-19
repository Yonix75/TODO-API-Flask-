from werkzeug.exceptions import NotFound, BadRequest, Conflict, UnprocessableEntity
from flask import jsonify, Blueprint, current_app

# Blueprint that keeps API errors returning JSON instead of HTML.
errors_bp = Blueprint("errrors", __name__)



@errors_bp.errorhandler(NotFound)
def handle_type_error(e):
    return jsonify({
        "error": str(e)
    }), 404

@errors_bp.errorhandler(BadRequest)
def handle_type_error(e):
    return jsonify({
        "error": str(e)
    }), 400
    
@errors_bp.errorhandler(UnprocessableEntity)
def handle_type_error(e):
    return jsonify({
        "error": str(e)
    }), 422
    
@errors_bp.errorhandler(ValueError)
def handle_type_error(e):
    return jsonify({
        "error": str(e)
    }), 422    