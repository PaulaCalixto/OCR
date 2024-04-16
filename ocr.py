import cv2
import pytesseract

img = cv2.imread("have-been.webp")

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

resultado = pytesseract.image_to_string(img)

print(resultado)

