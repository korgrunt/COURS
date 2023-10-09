from flask import Flask, request, jsonify, Response
from __init__ import DATABASE
from whisky import Whisky

app= Flask(__name__)
app.config['DEBUG'] = True

@app.route("/api/v1/whisky", methods=['GET'])
def whisky_all():
    w = Whisky(DATABASE)
    data = w.get_all()
    w.close_connection()
    return data

@app.route("/api/v1/whisky/<int:id>", methods=['GET'])
def whisky_one(id): 
    w = Whisky(DATABASE)
    data = w.get_one(id)
    w.close_connection()
    return jsonify(data)

@app.route("/api/v1/whisky", methods=['POST'])
def whisky_create(): 
    w = Whisky(DATABASE)
    print(request.get_json())
    w.create_one(request.get_json()['name'],request.get_json()['country'],request.get_json()['degree'],request.get_json()['region'],request.get_json()['price'])
    w.close_connection()
    return Response(status=201) 

@app.route("/api/v1/whisky/<int:id>", methods=['DELETE'])
def whisky_delete_one(id): 
    w = Whisky(DATABASE)
    w.delete_one(id)
    w.close_connection()
    return Response(status=204) 

@app.route("/api/v1/whisky/<int:id>", methods=['PUT'])
def whisky_update_one(id): 
    w = Whisky(DATABASE)
    w.update_one(id, request.get_json()['name'],request.get_json()['country'],request.get_json()['degree'],request.get_json()['region'],request.get_json()['price'])
    w.close_connection()
    return Response(status=204) 

@app.route("/api/v1/whisky/<int:id>", methods=['PATCH'])
def whisky_patch_one(id): 
    w = Whisky(DATABASE)
    w.patch_one(id, request.get_json())
    w.close_connection()
    return Response(status=204) 

if __name__ == "__main__":
    app.run()
