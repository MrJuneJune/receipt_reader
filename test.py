import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test.jpg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))
magnitude_spectrum[round(len(magnitude_spectrum)/2 - 600):round(len(magnitude_spectrum)/2 + 600)] = 0
reversed_magnitude_spectrum = np.abs(np.fft.ifft2(np.fft.ifftshift(magnitude_spectrum)))

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.subplot(123),plt.imshow(reversed_magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum without middle part'), plt.xticks([]), plt.yticks([])
plt.show()
