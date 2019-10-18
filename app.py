import json
import os

from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    respuesta = {"servidor-numero": 1}
    return jsonify(respuesta)


if __name__ == "__main__":
    puerto = int(os.environ.get("PYTHON1_PUERTO", 5000))
    app.run(host="0.0.0.0", port=puerto)


# # USADO POR GUNICORN
# def app(environ, start_response):

#     respuesta = {
#         "servidor-numero": 1
#     }

#     headers = [("Content-Type", "application/json")]
#     start_response("200 OK", headers)

#     return [bytes(json.dumps(respuesta), 'utf-8')]
