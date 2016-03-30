from flask import Flask, render_template, request
import CodingChallenge as cc
import json


app = Flask(__name__)	

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/process")
def process():
    ip = request.args.get("ip", "")
    subnet = request.args.get("subnet", "")
    try:
        res = cc.net_block(ip, subnet)
        res["success"] = True
        return json.dumps(res)
    except Exception as e:
        return json.dumps({"success": False})


if __name__ == "__main__":
    app.run(debug=True)
