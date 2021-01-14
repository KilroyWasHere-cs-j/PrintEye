import PIL
from PIL import ImageGrab

def grab(grab_all):
    if grab_all == True:
        return ImageGrab.grab(all_screens=True)
    else:
        return ImageGrab.grab(all_screens=False)

