import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import time as t
import Math
import UI


def interpret_output(pre):
    # This function is very much a sin, but I'm not changing it. Programing 101
    # This hardly works
    hold = pre.split(' ')
    hold = str(hold)
    hold.replace('[', '')
    hold.replace(']', '')
    items = hold.split()
    #for item in list1:
    #    print(item)
    one = items[0].replace('[[', '').replace('[', '')
    two = items[1].replace('[[', '')
    if one > two:
        print("One: ", one, two)
        print("Success")
    elif two > one:
        print("Two: ", two)
        print("Failure")
    else:
        print("Error")



def Process(camera):
    t0 = t.time()
    cap = cv2.VideoCapture(camera)
    holdover = cv2.imread("Success.jpg")
    while True:
        ret, frame = cap.read()
        #frame = cv2.imread("")
        np.set_printoptions(suppress=True)
        # Load the model
        model = tensorflow.keras.models.load_model('Prints.h5')
        # Create the array of the right shape to feed into the keras model
        # The 'length' or number of images you can put into the array is
        # determined by the first position in the shape tuple, in this case 1.
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        Math.MSE(frame, holdover)
        cv2.imwrite("Holdover.jpg", holdover)
        #cv2.imread("Frame.jpg", frame)
        holdover = frame
        # Replace this with the path to your image
        image = Image.fromarray(frame, 'RGB')
        # image = Image.open('Man.jpg')
        # resize the image to a 224x224 with the same strategy as in TM2:
        # resizing the image to be at least 224x224 and then cropping from the center
        size = 224, 224
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
        # turn the image into a numpy array
        image_array = np.asarray(image)
        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        # Load the image into the array
        data[0] = normalized_image_array
        # run the inference
        prediction = model.predict(data)
        pre = str(prediction)
        # print("predictionString", pre)
        t1 = t.time()
        print("\u001b[32mPrediction", prediction)
        print("\u001b[34mTime:", t1 - t0)
        if UI.Query_Config("showP - ") == "True":  # Doesn't work
            print("\u001b[32mPrediction", prediction)

            print("\u001b[34mTime:", t1 - t0)
        else:
            print("")
        interpret_output(pre=pre)
