import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

# Check the out put of the neural network
comp_Model_Path = ""
model_Prediction = ""
def neura_Test(preD, imPath, mPath):
    returnV = ""
    np.set_printoptions(suppress=True)
    # Load the model
    model = tensorflow.keras.models.load_model(mPath)

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open(imPath)

    # resize the image to a 224x224 with the same strategy as in TM2:
    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
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
    model_Prediction = pre
    # print("predictionString", pre)
    #print("prediction", prediction)
    try:
        if pre == preD:
            returnV = 0
        else:
            returnV = 1
    except:
        returnV = 2

    return returnV

def set_mPath(mPath):
    comp_Model_Path = mPath
    return "Model_Path_Set"


def nera_Prt(pre, imPath):
    retrunV = ""
    np.set_printoptions(suppress=True)
    # Load the model
    model = tensorflow.keras.models.load_model(comp_Model_Path)

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open(imPath)

    # resize the image to a 224x224 with the same strategy as in TM2:
    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
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
    #print("prediction", prediction)
    try:
        if pre == preD:
            retrunV = "Similar"
        else:
            returnV = "Not_Similar"
    except:
        retrunV = "Could_Not_Detrime_The_Simililty"

    return returnV

def prep_Prediction(pred):
    returnV = ""
    # Please don't look at this
    pred = pred.replace('[', '')
    pred = pred.replace(']', '')
    pred_Substring = pred.split(' ', 1)
    return pred_Substring

def num_Sim(pre):
    returnV = ""
    prediction = prep_Prediction(pred=pre)
    print("Output", prediction[0], prediction[1])
    try:
        print()
    except:
        print()
    output = "Hello World" # This is pointless, but I'm not removeing it fight me
    # for loop
    count = 0
    for i in prediction :
        count + 1
        if i == i[count]:
            returnV = 0
        else:
            returnV = 1

    return returnV

def I(x):
    round(x)

def normalize(x):
    ix = float(x)
    norm = 1 / (1 + np.exp(-ix))
    print("Normalized", x)



