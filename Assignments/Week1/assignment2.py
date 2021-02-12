from skimage import data, color, io
from skimage.viewer import ImageViewer 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter


def filterBlueColor(image : np.array):
    for row in image: 
        for col in  row:
            # Col is a list of r, g and b

            r = col[0]
            g = col[1]
            b = col[2]
    
            treshold = 0 # Modify treshold if needed
           
            if b > g and b > r and b-r > treshold and b-g > treshold:
                continue 
            

            y = 0.299*r + 0.587*g + 0.114*b 

            col[0] = y
            col[1] = y 
            col[2] = y
    return image


def histogramHSV(image : np.array):
    hues = [] 
    for row in image:
        for col in row:
            hues.append(col[0])
    
    plt.title("ALDS Week 1 - Histogram of HSV image")
    plt.ylabel("Count")
    plt.xlabel("Hue")
    plt.xlim(0, 1)
    plt.hist(x=hues, bins=255)
    plt.show()


imgpath = input("Image Location: ")
image = io.imread(imgpath)

# image = data.colorwheel()

hsvimg = color.rgb2hsv(image)
histogramHSV(hsvimg)

filtered_img = filterBlueColor(image)

hsvimg_filtered = color.rgb2hsv(filtered_img)

histogramHSV(hsvimg_filtered)

