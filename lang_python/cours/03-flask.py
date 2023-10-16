from flask import Flask, request, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=['GET'])
def home():
    return "welcome"




@app.route("/infos")
def infos():
    data = {
        "method": request.method,
        "headers": dict(request.headers),
        "path": request.path,
        "method": request.args,

    }
    return jsonify(data)

if __name__ == "__main__":
    app.run()
