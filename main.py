import cv2
import numpy as np
from PIL import ImageGrab

frames_per_second = 24

miliseconds_between_frames = int(1 / frames_per_second * 1000)

input_width_in_pixels = 1920
input_height_in_pixels = 1080

output_width_in_pixels = input_width_in_pixels // 2
output_height_in_pixels = input_height_in_pixels // 2

while True:
    complete_image = ImageGrab.grab(bbox=(0, 0, input_width_in_pixels, input_height_in_pixels))
    image_numpy = np.array(complete_image)
    
    height, width, channels = image_numpy.shape
    
    width_mid_point = width // 2
    left_half = image_numpy[:, :width_mid_point]
    right_half = image_numpy[:, width_mid_point:]

    difference = left_half - right_half
    difference_in_red = (difference != 0) * [255, 0, 0]

    highlited = np.clip(left_half + difference_in_red, None, 255)


    reshaped = cv2.resize(left_half, (output_width_in_pixels, output_height_in_pixels))
    cv2.imshow("helper", reshaped)

    if cv2.waitKey(miliseconds_between_frames) == ord('q'):
        break

cv2.destroyAllWindows()
