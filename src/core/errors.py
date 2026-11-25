from flask import request
from loguru import logger
from werkzeug.exceptions import HTTPException

from src.utils.api_errors import ApiError
from src.utils.error_codes import ErrCode
from src.core.response import fail


def register_errors(app):
    @app.errorhandler(ApiError)
    def api_error(exc):
        err_msg = exc.msg
        http_code = exc.http_code
        code = exc.code

        logger.info(
            '[app error] method={}, path={}, http_code={}, code={}, msg={}',
            request.method, request.path, http_code, code, err_msg,
        )
        return fail(err_msg, http_code, code)

    @app.errorhandler(HTTPException)
    def http_error(exc):
        err_msg = exc.description
        http_code = exc.code
        code = f'HTTP_{http_code}'

        logger.info(
            '[http error] method={}, path={}, http_code={}, msg={}',
            request.method, request.path, http_code, err_msg,
        )
        return fail(err_msg, http_code, code)

    @app.errorhandler(Exception)
    def server_error(exc):  # noqa
        err_msg = 'server error'
        http_code = 500
        code = ErrCode.SERVER_ERROR

        logger.exception('[server error] path={}', request.path)
        return fail(err_msg, http_code, code)
