from deepface import DeepFace
from PIL import Image
import cv2


def compare(img1, img2):
    """img = cv2.imread(img1)
    scale_percent = 20  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize image
    #img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    img3 = cv2.imread(img2)
    scale_percent = 20  # percent of original size
    width = int(img3.shape[1] * scale_percent / 100)
    height = int(img3.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize image
    #img3 = cv2.resize(img3, dim, interpolation=cv2.INTER_AREA)"""

    result = DeepFace.verify(img1_path=img1, img2_path=img2)

    return result['verified']


