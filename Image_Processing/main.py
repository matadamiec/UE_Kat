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
img_ocr_sample_1 = Image.open("OCR_Sample_1.jpg")
img_ocr_sample_1 = img_ocr_sample_1.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(img_ocr_sample_1)
img_ocr_sample_1 = enhancer.enhance(2)
img_ocr_sample_1 = img_ocr_sample_1.convert('1')
img_ocr_sample_1.save('temp_img_ocr_sample_1.jpg')
img_ocr_sample_1_text = pytesseract.image_to_string(Image.open('temp_img_ocr_sample_1.jpg'))
print("Zdjęcie 1:")
print(img_ocr_sample_1_text)
# OCR Sample 2:
img_ocr_sample_2 = Image.open("OCR_Sample_2.jpg")
img_ocr_sample_2 = img_ocr_sample_2.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(img_ocr_sample_2)
img_ocr_sample_2 = enhancer.enhance(2)
img_ocr_sample_2 = img_ocr_sample_2.convert('1')
img_ocr_sample_2.save('temp_img_ocr_sample_2.jpg')
img_ocr_sample_2_text = pytesseract.image_to_string(Image.open('temp_img_ocr_sample_2.jpg'))
print("Zdjęcie 2:")
print(img_ocr_sample_2_text)
# OCR Sample 3:
img_ocr_sample_3 = cv2.imread('OCR_Sample_3.jpg')
img_ocr_sample_3_text = pytesseract.image_to_string(img_ocr_sample_3)
print("Zdjęcie 3:")
print(img_ocr_sample_3_text)
# OCR Sample 4:
img_ocr_sample_4 = cv2.imread('OCR_Sample_4.jpg')
img_ocr_sample_4_text = pytesseract.image_to_string(img_ocr_sample_4)
print("Zdjęcie 4:")
print(img_ocr_sample_4_text)
# OCR Sample 5:
img_ocr_sample_5 = cv2.imread('OCR_Sample_5.jpg')
img_ocr_sample_5_text = pytesseract.image_to_string(img_ocr_sample_5)
print("Zdjęcie 5:")
print(img_ocr_sample_5_text)
