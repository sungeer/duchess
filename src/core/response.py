from flask import jsonify


def ok(data=None, http_status=200):
    return jsonify({
        'success': True,
        'data': data
    }), http_status


def fail(message: str, http_status: int, code: str):
    return jsonify({
        'success': False,
        'code': code,
        'message': message
    }), http_status
