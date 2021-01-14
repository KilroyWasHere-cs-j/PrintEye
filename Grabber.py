import PIL
from PIL import ImageGrab

# No in use yet
def grab(grab_all):
    if grab_all == True:
        return ImageGrab.grab(all_screens=True)
    else:
        return ImageGrab.grab(all_screens=False)

