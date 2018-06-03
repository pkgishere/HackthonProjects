from datetime import datetime
from flasgger import Swagger
from flask import Flask, jsonify, abort, make_response, request, render_template
from flask_restful import Api, Resource, reqparse, fields, marshal
from OpenSSL import SSL
from serviceEndpoints.mySafeApi import MySafeApi

app = Flask(__name__)
api = Api(app)
app.config['SWAGGER'] = {
    'title': 'Proxyfier API',
    'uiversion': 2
}
swagger = Swagger(app)

context = SSL.Context(SSL.SSLv23_METHOD)
context.use_privatekey_file('sparkysvision.key')
context.use_certificate_file('sparkysvision.crt')

# CRAWLER ENDPOINTS
#----------------------------------------------------------------
api.add_resource(MySafeApi, '/visionAPI/proxyfier')

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=80, ssl_context=context)
    # app.run(host='0.0.0.0',port=80)
    app.run(host='0.0.0.0', port=80, ssl_context=('sparkysvision.crt', 'sparkysvision.key'))
    #app.run(host='127.0.0.1', debug=True, ssl_context=context)
