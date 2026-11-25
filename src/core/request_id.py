import uuid

from flask import g

from src.core.ctx import request_id_var


def register_request_id(app):
    @app.before_request
    def attach_request_id():
        request_id: str = uuid.uuid4().hex[:18]
        g.request_id = request_id
        request_id_var.set(request_id)

    @app.after_request
    def echo_request_id(response):
        request_id = g.get('request_id', '')
        response.headers['X-Request-ID'] = request_id
        return response
