import imageio as img
import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Users\\komputer jarkom 2\\Pictures\\Negatif.jpeg"

imgNegatif = img.imread(path)
redNegatif = imgNegatif[:,:,0]
rN_hist, bins = np.histogram(redNegatif,bins=256,range=[0,256])


imgPositif = 255 - imgNegatif
redPositif = imgPositif[:, :, 0]
rP_hist, _ = np.histogram(redPositif, bins=256, range=[0, 256])

plt.figure(figsize=(10, 10))

plt.subplot(2, 2, 1)
plt.imshow(imgNegatif)
plt.title("Negative Image")

plt.subplot(2, 2, 2)
plt.imshow(imgPositif)
plt.title("Positive Image")

plt.subplot(2, 2, 3)
plt.plot(rN_hist, color='red', label='Red Histogram (Negative)')
plt.title("Red Channel Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.legend()
plt.subplot(2, 2, 4)
plt.plot(rP_hist, color='blue', label='Red Histogram (Positive)')
plt.title("Red Channel Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.legend()

plt.tight_layout()
plt.show()


