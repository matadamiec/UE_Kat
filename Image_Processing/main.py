import cv2
import pytesseract as pytesseract
from PIL import Image, ImageEnhance, ImageFilter

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# img = cv2.imread('e38.jpg')
# print('type(img):')
# print(type(img))
# print('img.shape')
# print(img.shape)
# img_convert = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('image', img)
# cv2.imshow('image', img_convert)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# OCR Sample 1:
print("Zdjęcie 1:")
print(pytesseract.image_to_string(Image.open("OCR_Sample_1.jpg")))
# OCR Sample 2:
print("Zdjęcie 2:")
print(pytesseract.image_to_string(Image.open("OCR_Sample_2.jpg")))
# OCR Sample 3:
print("Zdjęcie 3:")
print(pytesseract.image_to_string(cv2.imread('OCR_Sample_3.jpg')))
# OCR Sample 4:
print("Zdjęcie 4:")
print(pytesseract.image_to_string(cv2.imread('OCR_Sample_4.jpg')))
# OCR Sample 5:
print("Zdjęcie 5:")
print(pytesseract.image_to_string(cv2.imread('OCR_Sample_5.jpg')))
