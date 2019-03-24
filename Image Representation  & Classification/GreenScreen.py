import numpy as np
import matplotlib.pyplot as plt
import cv2


img = cv2.imread('images/car_green_screen.jpg')

img_copy = np.copy(img)
img_copy = cv2.cvtColor(img_copy, cv2.COLOR_BGR2RGB)

# plt.imshow(img_copy)
# plt.show()

# first things we define lower and upper bound

lower_green = np.array([0, 50, 0])
upper_green = np.array([110, 255, 110])

# make mask to select car
mask = cv2.inRange(img_copy, lower_green, upper_green)
# plt.imshow(mask, cmap="gray")
# plt.show()

masked_image = np.copy(img_copy)
masked_image[mask != 0] = [0, 0, 0]
# plt.imshow(masked_image)
# plt.show()

# read background
sky_img = cv2.imread("images/sky.jpg")
sky_img = cv2.cvtColor(sky_img, cv2.COLOR_BGR2RGB)
sky_img = sky_img[: img.shape[0], : img.shape[1]]

# apply mask in background

sky_img[mask == 0] = [0, 0, 0]
# plt.imshow(sky_img)
# plt.show()

# add 2 images
comlete_image = sky_img + masked_image
plt.imshow(comlete_image)
plt.show()