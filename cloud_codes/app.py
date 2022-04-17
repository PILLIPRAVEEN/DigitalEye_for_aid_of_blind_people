from flask import Flask, request, jsonify
from facerecog import recog
from objdetect import obj_detect
import os

app = Flask(__name__)
@app.route("/")
def home():
    return "Homepage"
@app.route("/face_recognition", methods=["GET", "POST"])

def send_face():
    if request.method == "GET":
        return jsonify({"status_code":201})

    if request.method == "POST":
            file_ = request.files['image']
            print("Image recieved!")
            file_.save('in_image.jpg')

            detection = recog("in_image.jpg")

            print({"prediction":detection})
            return jsonify({"prediction":detection})

@app.route("/object_recognition", methods=["GET", "POST"])
def send_obj():
    if request.method == "GET":
        return jsonify({"status_code":201})
    if request.method == "POST":
        file_ = request.files['image']
        print("Image recieved!")
        file_.save('in_image.jpg')

        detection = obj_detect("in_image.jpg")

        print({"prediction":detection})
        return jsonify({"prediction":detection})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

