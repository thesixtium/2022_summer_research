import math
import cv2
import numpy as np
from matplotlib import pyplot as plt


def y_positive(x, y, w, h):
    x_pos = math.floor((76 / 353) * w) + x
    y_pos = math.floor((68 / 215) * h) + y
    return [x_pos, y_pos]


def y_negative(x, y, w, h):
    x_pos = math.floor((76 / 353) * w) + x
    y_pos = math.floor((148 / 215) * h) + y
    return [x_pos, y_pos]


def x_positive(x, y, w, h):
    x_pos = math.floor((103 / 353) * w) + x
    y_pos = math.floor((112 / 215) * h) + y
    return [x_pos, y_pos]


def x_negative(x, y, w, h):
    x_pos = math.floor((33 / 353) * w) + x
    y_pos = math.floor((112 / 215) * h) + y
    return [x_pos, y_pos]


def x_steps(x, y, w, h):
    x_pos = math.floor((233.5 / 353) * w) + x
    y_pos = math.floor((81 / 215) * h) + y
    return [x_pos, y_pos]


def y_steps(x, y, w, h):
    x_pos = math.floor((233.5 / 353) * w) + x
    y_pos = math.floor((104 / 215) * h) + y
    return [x_pos, y_pos]


def movement_gui_positions(x, y, w, h):
    return_dictionary = {
        "y_positive": y_positive(x, y, w, h),
        "y_negative": y_negative(x, y, w, h),
        "x_positive": x_positive(x, y, w, h),
        "x_negative": x_negative(x, y, w, h),
        "x_steps": x_steps(x, y, w, h),
        "y_steps": y_steps(x, y, w, h)
    }

    return return_dictionary


def laser_window_positions(base_image, what_to_find):
    img_rgb = cv2.imread(base_image)  # Base image
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(what_to_find, 0)  # What to match
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.3
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    image_name = "z" + what_to_find[:-4] + '_result.png'
    cv2.imwrite(image_name, img_rgb)
    return image_name
