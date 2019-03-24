import numpy as np
import matplotlib.pyplot as plt
import cv2


# read image
image = cv2.imread("images/pizza_bluescreen.jpg")

# first we print the shape of image
# 514, 816, 3
print(image.shape)

img_copy = np.copy(image)
# convert image from BGR to RGB
img_copy = cv2.cvtColor(img_copy, cv2.COLOR_BGR2RGB)
# plt.imshow(img_copy)
# plt.show()


# we define the lower and upper bound for blue color in image

lower_blue = np.array([0, 0, 220])
upper_blue = np.array([50, 70, 255])

# we create image mask to select interstion area of image
mask = cv2.inRange(img_copy, lower_blue, upper_blue)
# it return b&w image if the pixel value in range make it white else make it black
# plt.imshow(mask, cmap="gray")
# plt.show()

masked_image = np.copy(img_copy)
masked_image[mask != 0] = [0, 0, 0]
# plt.imshow(masked_image)
# plt.show()

back_image = cv2.imread("images/space_background.jpg")
back_image = cv2.cvtColor(back_image, cv2.COLOR_BGR2RGB)

# crop background image
crop_back = back_image[:image.shape[0], :image.shape[1]]

crop_back[mask == 0] = [0, 0, 0]
# plt.imshow(crop_back)
# plt.show()

complete_image = masked_image + crop_back

plt.imshow(complete_image)
plt.show()