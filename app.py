import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
app=Flask(__name__)
app.config["MAX_CONTENT_LENGTH"]=100*1024*1024
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/health")
def health():
    return jsonify(status="ok")
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
