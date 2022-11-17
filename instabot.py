from flask import Flask,Blueprint, request, json, jsonify
from flask_ngrok import run_with_ngrok
import sqlite3
import random
#########################
app = Flask(__name__)
run_with_ngrok(app)
#########################
@app.route("/log",methods=["GET", "POST"])
def log():
   d={}
   name = request.form.get('name')
   id = request.form.get('id')
   if name=="fadi":
        print("sucsses ")
        return jsonify(d)
   else:
        print("ss")
        return jsonify(d)
#########################  
if __name__ == "__main__":
    app.run()
