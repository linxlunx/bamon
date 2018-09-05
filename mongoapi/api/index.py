#!/bin/bash

from pymongo import MongoClient
from flask import Flask, request, Response, jsonify
from bson.objectid import ObjectId
from flask_cors import CORS
import json
import re

client = MongoClient(host="mongodb")
db = client["universalApi"]

app = Flask(__name__)
CORS(app)

@app.route("/<collection>")
def index(collection):
    params = request.args
    
    if not params:
        data_list = db[collection].find()
    else:
        filters = []
        for param in params:
            temp = {}
            if param == 'name':
                temp[param] = {"$regex": "^{}".format(params[param])}
            else:
                temp[param] = params[param]
            filters.append(temp)

        data_list = db[collection].find(
            {
                "$and": filters
            }
        )

    data_collection = []
    for data in data_list:
        data['_id'] = str(data['_id'])
        data_collection.append(data)

    result = {
        "collection": collection,
        "data": data_collection,
    }

    return jsonify(result)

@app.route("/<collection>/<id>")
def detail(collection, id):
    try:
        single_data = db[collection].find_one({
            '_id': ObjectId(id)
        })
    except:
        single_data = False

    if not single_data:
        data = {}
    else:
        single_data['_id'] = str(single_data['_id'])
        data = single_data
    
    result = {
        "collection": collection,
        "data": data,
        "id": id
    }

    return jsonify(result)

@app.route("/<collection>/insert", methods=["POST"])
def insert(collection):
    if request.method == "POST":
        data = request.form.get("data")

        if data is None:
            return jsonify({
                "error": "please submit data"
            })
        
        try:
            post_data = json.loads(data)
        except:
            return jsonify({
                "error": "please submit json format"
            })

        db[collection].insert(post_data)
        
        post_data["_id"] = str(post_data["_id"])
        
        result = {
            "collection": collection,
            "data": post_data,
        }

        return jsonify(result)

@app.route("/<collection>/<id>/edit", methods=["POST"])
def edit(collection, id):
    if request.method == "POST":
        data = request.form.get("data")

        if id is None:
            return jsonify({
                "error": "please submit data"
            })
        try:
            col_id = ObjectId(id)
        except:
            return jsonify({
                "error": "please submit correct id format"
            })

        try:
            post_data = json.loads(data)
        except:
            return jsonify({
                "error": "please submit json format"
            })

        col_data = db[collection].find_one({"_id": col_id})
        if not col_data:
            return jsonify({
                "error": "id not found"
            })
        else:
            col_update = db[collection].update_one({
                "_id": col_id
            }, {
                "$set": post_data
            })

        col_data = db[collection].find_one({"_id": col_id})
        col_data["_id"] = str(col_data["_id"])

        result = {
            "collection": collection,
            "data": col_data,
        }

        return jsonify(result)

@app.route("/<collection>/<id>/delete")
def delete(collection, id):
    db[collection].remove({
        "_id": ObjectId(id)
    })

    result = {
        "collection": collection,
        "_id": id,
        "status": "deleted"
    }
    return jsonify(result)

if __name__== "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
