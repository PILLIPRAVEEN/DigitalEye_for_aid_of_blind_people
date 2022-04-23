                                                 DIGITAL EYE FIR AID OF BLIND PEOPLE

PROJECT DESCRIPTION :
          This project is designed for blind people or visually impaired people using DE 10 nano FPGA board, RFS card and Azure Cloud.
          This project aims to resemble the role of our present technology in improving the status of living conditions of blind people.
          Using this project a guidance system can be provided to the blind in safely reaching to a destination and to recognize and to 
          save the faces of known people such as famiily and firends etc. and to recognize objects and avoid the obstacles in the path 
          and to recognize and read text and finally to recognize the currency.
          So here we has divided the complete project into 5 blocks which includes a time limit to terminate. And 5 external triggers are
          enabled for 5 different tasks. If only single block is activated, then the program is designed in such a way that the it will be
          executed for 30 minutes of duration (except navigation block). But if two or more blocks are activated at once then the priority
          conditions will be taken into consideration. According to their priority, the corresponding block will be executed first for a 
          duration of 1 minute (except navigation block). And the while procedure will be repeated continuosly to have a periodic execution
          all blocks continiously which inturn reduces the delay due to the unifunctional existance of the device at a time.
          
          Blocks of our project:
          
          1. NAVIGATION AND VEHICLE AVOIDANCE BLOCK :
          
          When the navigation block is activated, the device asks for the user's destination and recieves the destination name through serial communication
          Coordinates will be fetched from the destination name from geocoders and the shortest path will be mapped from the user's current coordinate to 
          the destination using postman API from the azure maps.
          And based on the user's deviation angle and the angle between shortest distance coordinate to the user's current coordinate the angle will be fetched 
          and directed using octa-polar segmentation. And meanwhile if there are any vehicle or pedestrians detected in the path can be easily predicted in advace
          and avoiding directions will be generated based on the cntral coordinates region in the segment bounding box.
          
          2.FACE DETECTION AND RECOGNITION BLOCK :
          
          When this block is activated then then the face detection algorithm starts to work along with the distance predictions based on the
          dimensional ratio aspects. And if any face is inside the distance range then the detection count increases  and if the count reaches to a
          limit, then immediately face recogntion algorithm starts and if the face is matched with any of the saved faces then it will emit a voice output
          with the name of the person that he/she is infront of the user. If the face is not recognized the deivce asks the user to save the face of the 
          person or not. If the user's choice is yes, then the device asks for the name of the person and saves the face with the reiceved name in the saved faces.
          
          3.OBJECT DETECTION AND OBSTACLE AVOIDANCE BLOCK :

          When this is block is activated then the captured frame will be sent to the processing unit of the cloud craeted using a linux based Docker and the 
          correspodning output will be retrieved. The processing will be completely based on the tensorflow and cvlib which uses 80 pretrained models of YOLOV3
          dataset. And based on the labels of the detected objects the objects will be segregated into obstacles or not and each and every object will be stated
          with their names along with their direction of existance. Based on the coordinates of the bounding boxes the user will be directed to aviid the obstacle in the path.

          4.OPTICAL CHARACTER RECOGNIZATION BLOCK :
          
          This block is completely dependent on the tesseract OCR and pytesseract modules. When this block gets activated, the frame will be subjected to
          BGR to HSV color conversion and the tesseract fuction willl be initialzed. And the frame will be perfomed threshold operation and applied by dilation and 
          then the dilated image will be bounded by a rectangle in whhich the while sentense is captured. And after the capturing of the all the text, it will fed to the 
          voice output multiplexing unit. And if the same text is found to be repeating for the next frame, then the device sets for a trigger that the same frme is
          repeated, and asks for the user to read it again. Based on the choice of the user, it will be read or neglected.
          
          5.CURERNCY RECOGNTION BLOCK :
          
          It is a basic algorithm works on the basis of face recogntion and text recogntion. When this block is activated, then the face detection unit will be on. And
          if a face is detected, it activated the face recogntion unit and the face o the currency will be compared with stored faces of national leaders of different currency.
          and if the face is matched, then the text detection unit will be activated for first line of the currency. And based on the detected text on the 
          currency and the face on the currency, the value and the type of currency will be determined and sends to voice output.
