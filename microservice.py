import os
from flask import Flask, send_file
from flask_restful import Api, Resource

app = Flask(name)
api = Api(app)

IMAGE_FOLDER = "./Images/"

class Image(Resource):
    def get(self, filename):
        return send_file(os.path.join(IMAGE_FOLDER, filename), mimetype='image/jpeg')

class ImageList(Resource):
    def get(self):
        images = os.listdir(IMAGE_FOLDER)
        return {'images': images}

api.add_resource(Image, '/image/<string:filename>')
api.add_resource(ImageList, '/images')

if __name__ == "main":
    app.run(host="0.0.0.0", port=8080)

