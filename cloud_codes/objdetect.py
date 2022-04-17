import cv2
import cvlib as cl
from cvlib.object_detection import draw_bbox

obj_detect_url = "http://Dgital_Eye.azurewebsites.net/object_recognition"
def obj_detect(img1):
    img=cv2.imread(img1)
    bx,lbl,cnf=cl.detect_common_objects(img)
    img1=draw_bbox(img,bx,lbl,cnf)
    print(bx)
    return([lbl,bx])