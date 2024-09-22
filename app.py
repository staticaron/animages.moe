from flask import Flask, send_file, render_template, jsonify, request, abort
import socket
import os
import datetime
import random

app = Flask("animages.moe")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<username>/<collection>.png", methods=['GET'])
def send_main(username, collection):
    
    path = f"static/images/{username}/{collection}/"
    
    files = os.listdir(path)
    
    r_value = random.randint(0, len(files) - 1)
    
    selected_file_path = path + files[r_value]
    
    print(datetime.datetime.now().__str__())
    
    return send_file(selected_file_path, mimetype="image/png")

@app.route("/api/assets", methods=["GET"])
def send_assets():
    
    this_IP = socket.gethostbyname( socket.gethostname() )
    
    print(f"Base IP : {this_IP}")
    print(f"Request IP : {request.remote_addr}")
    
    if this_IP != request.remote_addr and request.remote_addr != "127.0.0.1":
        abort(403)
    
    def get_response(path):
        
        print(f"Looking into : {path}")
        
        directory = os.listdir(path)
    
        response = {
            "files" : []
        }
        
        for i in directory:
            
            is_file = os.path.isfile(path + i)
            
            if is_file:    
                response["files"].append(
                    {
                        "path" : path + i
                    }
                )

            else:
                holder = get_response(path + i + "/")
                
                response["files"].extend(holder["files"])

        return response

    path = "static/assets/"
    
    return jsonify(get_response(path))