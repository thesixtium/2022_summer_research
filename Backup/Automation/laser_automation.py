import cv2
import numpy as nm
import pytesseract
import re


def get_values(image, template):
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    img = cv2.imread(image, 0)
    img2 = img.copy()
    template = cv2.imread(template, 0)
    w, h = template.shape[::-1]

    img = img2.copy()
    method = eval('cv2.TM_CCOEFF_NORMED')

    # Apply template Matching
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    cropped = img[top_left[1] + 20:top_left[1] + h - 100, top_left[0]:top_left[0] + w + 100]

    tesstr = pytesseract.image_to_string(nm.array(cropped), lang='eng')
    return format_values(tesstr)


def format_values(string):
    string = string.split("\n")
    split_array = []
    for line in string:
        if line != "":
            split_array.append(str(re.search("[\d]+\.[\d]+", line).group()))
    return_dict = {
        "Total Signal": split_array[0],
        "Normal Force": split_array[1],
        "Lateral Force": split_array[2],
        "Peak Amplitude": split_array[3]
    }
    return return_dict


if __name__ == '__main__':
    print(get_values("ss1.PNG", "t2.PNG"))
