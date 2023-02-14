import os
from flask import Flask, send_from_directory

app = Flask(__name__)
IMAGE_FOLDER = "images"
app.config["UPLOAD_FOLDER"] = IMAGE_FOLDER

@app.route("/images/<path:filename>")
def get_image(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)


