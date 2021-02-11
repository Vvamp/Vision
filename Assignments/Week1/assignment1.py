from skimage import data 
from skimage.viewer import ImageViewer 
import numpy as np

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

image = data.colorwheel()
# image = data.astronaut()
filterBlueColor(image)


viewer = ImageViewer(image)
viewer.show()
