import imageio as img
import numpy as np
import matplotlib.pyplot as plt

def bright(image,factor):
    imgBright = image.astype(np.float32)
    imgBright = imgBright + factor
    imgBright = np.clip(imgBright,0,255)
    return imgBright.astype(np.uint8)

def contrast(image,factor):
    mean = 128
    imgContrast = image.astype(np.float32)
    imgContrast = mean + factor * (imgContrast - mean)
    imgContrast = np.clip (imgContrast,0,255)
    return imgContrast.astype(np.uint8)

path = "C:\\Users\\komputer jarkom 2\\Pictures\\pemandangan.jpg"
image = img.imread(path)

imgBright = bright(image,50)
imgContrast = contrast(image,1.5)

plt.figure(figsize=(10,10))
plt.subplot(3,1,1)
plt.imshow(image)

plt.subplot(3,1,2)
plt.imshow(imgBright)

plt.subplot(3,1,3)
plt.imshow(imgBright)


plt.show()