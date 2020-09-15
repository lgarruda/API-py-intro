# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 12:54:35 2020

@author: lgarr
"""

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {"about": "Hello World!"}
    
    def post(self):
        some_json = request.get_json()
        return {"You sent": some_json}, 201

class Multi(Resource):
    def get(self, num):
        return {"Resultado": num*10}

api.add_resource(HelloWorld, "/")
api.add_resource(Multi, "/multi/<int:num>")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True, use_reloader=False)
