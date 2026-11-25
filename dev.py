import logging

from app import app

logging.getLogger('werkzeug').disabled = True

app.run(
    host='127.0.0.1',
    port=8848
)
