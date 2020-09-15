# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 11:32:30 2020

@author: lgarr
"""


from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def Index():
    if(request.method == 'POST'):
        some_json = request.get_json();
        return jsonify({"You sent": some_json}), 201
    else:
        return jsonify({"About": "Hello World!"})

@app.route('/multi/<int:num>', methods=['GET'])
def get_multiply10(num):
    return jsonify({"Resultado":num*10})

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True, use_reloader=False)
