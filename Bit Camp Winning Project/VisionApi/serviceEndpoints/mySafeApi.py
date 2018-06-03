import json
from flask_restful import Resource, request
from flask import Flask, request, jsonify, _request_ctx_stack, redirect


class MySafeApi (Resource):

    def post(self):
        """Proxy interface between Google API and Google cloud http server
        Implemented in flask for python 2.7
        ---
        parameters:
          - name: requestHeader
            in: header
            type: string
            required: false
            default: 
            description: Everything from home mini
          - name: requestBody
            in: body
            type: string
            required: false
            default: 
            description: Everything from home mini
        operationId: proxyLayerForHomeMini
        consumes:
          - string
        produces:
          - string

        deprecated: false
        externalDocs:
          description: Project repository
          url: https://github.com/snarang2/HackBitcamp18
        responses:
          200:
            description: Parse Slack archive and save data to database
        """
        requestHeader = request.headers.get('requestHeader')
        requestBody = request.headers.get('requestBody')
        redirectionUrl = 'http://www.google.com'
        return redirect(redirectionUrl)
