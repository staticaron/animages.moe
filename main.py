from flask import Flask, send_file
import random

app = Flask("animages.moe")

@app.route("/")
def home():
    return "<h1>animages.moe</h1>"

@app.route("/main")
def main_page():
    return "Main Page"

@app.route("/main/main.png", methods=['GET'])
def send_main():
    r_value = random.randint(0, 1)
    
    if r_value == 0:
        return send_file("images/main/art1.png", download_name="file.png", mimetype="image/png")
    else:
        return send_file("images/main/art2.png", download_name="file.png", mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True)