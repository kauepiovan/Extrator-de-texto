import os
import cv2 as cv
import pytesseract
from dotenv import load_dotenv

load_dotenv()

# Pega o path das variaveis de ambiente
tesseract_path = os.getenv("TESSERACT_PATH")
image_path = os.getenv("IMAGE_PATH")
image_name = os.getenv("IMAGE_NAME")

pytesseract.pytesseract.tesseract_cmd = f'{tesseract_path}'

# Armazena a imagem em uma variavel
img = cv.imread(f'{image_path}{image_name}')
texto = pytesseract.image_to_string(img, lang='por')

print(texto)
