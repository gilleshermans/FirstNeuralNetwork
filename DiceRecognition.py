import numpy as np
from random import randint
from PIL import Image

def get_data():
    num = randint(1, 6)
    file = str(randint(0, 199))

    # Reformating => The file name is correct
    zeros = ""
    for i in range(5-len(file)):
        zeros += "0"
    file = zeros + file

    # Get the image (128x128)
    img = np.array(Image.open("DiceDataset/{}/{}.bmp".format(num, file)))
    return img, num
    

