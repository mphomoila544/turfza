
from PIL import Image
from pytesseract import pytesseract


def extractText(img):
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image_path = img

    img = Image.open(image_path)

    pytesseract.tesseract_cmd = path_to_tesseract

    text = pytesseract.image_to_string(img)

    return text


# lepotoalfred18@gmail.com
