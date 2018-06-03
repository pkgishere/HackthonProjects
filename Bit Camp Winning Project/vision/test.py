from PIL import Image
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
# img = Image.open("documentVision.jpg")
# rgb = img.convert('RGB')
# pix = img.load()
# print(dir(pix))

# for x in range(img.size[0]):
#     for y in range(img.size[1]):
#         #r, g, b, = rgb.getpixel((x, y))
#         r, g, b, = pix[x,y]
#         if r >= 245 and g >= 245:
#         	print x,y, r, g, b
#         	print "Yellow"
#         	# break
#         else:
#         	# rgb.setpixel((x, y))=[0,0,0]
#          	pix[x,y] = (0,0,0)
# #         # numpy.add
image = cv2.imread("documentVision.jpg")
# a = numpy.asarray(pix) 
# cv2.imshow('image', a)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# print im
# # print(type(pix))
# # im.show()
# plt.plot(im)
# plt.show()
# # print dir(rgb.putpixel)       		# hs.add((x,y))


yellow = np.array([255, 255, 0])
# image = np.zeros((400,400,3), dtype="uint8")
raw = image.copy()
# print image
image[np.where((image>[251,255, 105]).all(axis=2))] = [0,0,0]

yellowIndex = np.where(np.equal(image, yellow))
cv2.imshow('Test', image)
cv2.imshow('Test2', raw)
if cv2.waitKey() == ord('q'):
	cv2.destroyAllWindows()