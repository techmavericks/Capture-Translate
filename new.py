from flask import Flask,request,jsonify
import pytesseract
import requests
from PIL import Image
from PIL import ImageFilter
from io import StringIO
import os
import logging
from logging import Formatter, FileHandler
from googletrans import Translator
translator = Translator()
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
app = Flask(__name__)
@app.route('/', methods=["POST","GET"])
def ocr():
    try:
        url = request.json['image_url'][0]
        if 'jpg' in url:
            image = Image.open(url)
            return pytesseract.image_to_string(image,lang="Tamil")
        else:
            return jsonify({"error": "only .jpg files, please"})
    except:
        return jsonify({"error": "Did you mean to send: {'image_url': 'some_jpeg_url'}"})
    
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host ="0.0.0.0",debug=False,port=port)
