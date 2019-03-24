import numpy as np
import matplotlib.pyplot as plt
import cv2

image = cv2.imread("images/water_balloons.jpg")
# plt.imshow(image)
# plt.show()
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

r = image[:, :, 0]
g = image[:, :, 1]
b = image[:, :, 2]

# f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 10))
# ax1.set_title("red")
# ax1.imshow(r, cmap="gray")
#
# ax2.set_title("green")
# ax2.imshow(g, cmap="gray")
#
# ax3.set_title("blue")
# ax3.imshow(b, cmap="gray")
#
# plt.show()


# convert from RGB to HSV

hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
h = hsv[:, :, 0]
s = hsv[:, :, 1]
v = hsv[:, :, 2]

# f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 10))
# ax1.set_title("Hue")
# ax1.imshow(h, cmap="gray")
#
# ax2.set_title("Saturation")
# ax2.imshow(s, cmap="gray")
#
# ax3.set_title("Value")
# ax3.imshow(v, cmap="gray")
#
# plt.show()

# get mask by rgb

lower_pink = np.array([180, 0, 100])
upper_pink = np.array([255, 255, 230])

rgb_mask = cv2.inRange(image, lower_pink, upper_pink)
image[rgb_mask == 0] = [0, 0, 0]

# plt.imshow(image)
# plt.show()

lower_hue = np.array([160, 0, 0])
upper_hue = np.array([180, 255, 255])

hsv_mask = cv2.inRange(hsv, lower_hue, upper_hue)
hsv[hsv_mask == 0] = [0, 0, 0]

plt.imshow(hsv)
plt.show()

