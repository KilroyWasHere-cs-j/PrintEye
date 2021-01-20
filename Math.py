import numpy as np
import FileHandlers as FH


def Sig(x):
    return 1 / (1 + np.exp(-x))


def MSE(imageA, imageB):
    try:
        # the 'Mean Squared Error' between the two images is the
        # sum of the squared difference between the two images;
        # NOTE: the two images must have the same dimension
        err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
        err /= float(imageA.shape[0] * imageA.shape[1])

        # return the MSE, the lower the error, the more "similar"
        # the two images are
        #print("MSE: ", err)
        #print("MSE Sigmoid: ", Sig(err))
        return err
    except:
        FH.Update_Log("frame and holdover were not the same size")
        return 111.111


def UpdateTime(t):
    return "Updated"

