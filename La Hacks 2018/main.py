from flask import Flask
from OpenSSL import SSL

import os

from werkzeug.serving import make_ssl_devcert
# make_ssl_devcert('key', host='localhost')
make_ssl_devcert('key')

context = SSL.Context(SSL.SSLv23_METHOD)
cer = os.path.join(os.path.dirname(__file__), 'key.crt')
key = os.path.join(os.path.dirname(__file__), 'key.key')

app = Flask(__name__)


@app.route('/')
def hello_world():
	return 'Hellokjnkj World!'


if __name__ == '__main__':
	context = (cer, key)
	app.run(host='0.0.0.0', port=5000, debug=True, ssl_context=context)

