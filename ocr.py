# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
	help="type of preprocessing to be done")
args = vars(ap.parse_args())

# load the example image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray1,100,200)
print(gray)

# check to see if we should apply thresholding to preprocess the
# image
if args["preprocess"] == "thresh":
#	gray = cv2.threshold(gray, 175,255,cv2.THRESH_TOZERO_INV)[1]
	gray = cv2.threshold(gray, 0, 255,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# 	gray = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
# 	gray = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
#            cv2.THRESH_BINARY,11,2)



# make a check to see if median blurring should be done to remove noise
elif args["preprocess"] == "blur":
	gray = cv2.medianBlur(gray, 3)

# write the grayscale image to disk as a temporary file so we can
# apply OCR to it

filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file

text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)

# show the output images
og_img=cv2.resize(image, (0,0), fx=0.2, fy=0.1)
og_img_gray=cv2.resize(gray, (0,0), fx=0.2, fy=0.1)
og_img_gray1=cv2.resize(gray1, (0,0), fx=0.2, fy=0.1)
og_img_canny=cv2.resize(edges, (0,0), fx=0.2, fy=0.1)

cv2.imshow("Image", og_img_canny)
#cv2.imshow("Image", og_img)
cv2.imshow("Output", og_img_gray)
cv2.imshow("Gray", og_img_gray1)
cv2.waitKey(0)
