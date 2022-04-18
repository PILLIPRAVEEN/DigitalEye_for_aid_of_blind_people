#                                   FUNCTIONALITIES OF THE CODE

#This code uses the predefined functions of Face recognition and object recognitions written in the local machine folder.
#This code assigns two unique URLs and seperate routes for both operations.
#If a read image is fed to the function it will be first saved and fed back to the both face recognition unit and onject
#  recongnition unit.
#The predictions of the functions are return back in the json dictionary format with the predicted names of the persons and objects.

#For sending and recieving the requests and predictions of the functions
from flask import Flask, request, jsonify
#Face recongnition fucntion
from facerecog import recog
#Object recognition function
from objdetect import obj_detect
import os

app = Flask(__name__)
@app.route("/")
def home():
    return "Homepage"
#Route of the face recognition models
@app.route("/face_recognition", methods=["GET", "POST"])

#Function to send the read image of a face
def send_face():
    if request.method == "GET":
        return jsonify({"status_code":201})

    if request.method == "POST":
            file_ = request.files['image']
            print("Image recieved!")

            #Saving the read face image
            file_.save('in_image.jpg')

            #Applying the face recognition function
            detection = recog("in_image.jpg")

            print({"prediction":detection})

            #Returning the prediction in the json fomrat
            return jsonify({"prediction":detection})


#Route of object recognition 
@app.route("/object_recognition", methods=["GET", "POST"])
def send_obj():
    if request.method == "GET":
        return jsonify({"status_code":201})
    if request.method == "POST":
        file_ = request.files['image']

        print("Image recieved!")
        #Saving the recieved image
        file_.save('in_image.jpg')

        #Applying object detection function on the saved image.
        detection = obj_detect("in_image.jpg")

        print({"prediction":detection})
        #Returning predictions in the json format.
        return jsonify({"prediction":detection})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
