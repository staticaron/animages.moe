import pdb
from flask import Flask, send_file
import os
import random

app = Flask("animages.moe")

@app.route("/")
def home():
    return "<h1>animages.moe</h1>"

@app.route("/<username>/<collection>.png", methods=['GET'])
def send_main(username, collection):
    
    path = f"images/{username}/{collection}/"
    
    files = os.listdir(path)
    
    r_value = random.randint(0, len(files) - 1)
    
    selected_file_path = path + files[r_value]
    
    return send_file(selected_file_path, mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True)