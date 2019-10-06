from flask import Flask,request,jsonify
import pytesseract
import requests
import werkzeug
import os
from PIL import Image
from googletrans import Translator
translator = Translator()
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
app = Flask(__name__)

@app.route('/translate',methods=['GET','POST'])
def index():
    text = request.json['text']
    language = request.json['lancode']
    a = translator.translate([text], dest=language)
    for i in a:
         translated_text= i.text
    return  translated_text

@app.route('/image', methods=["POST","GET"])
def image():
        imagefile = request.files['image']
        lancode = request.json['lncode']
        image = Image.open(imagefile)
        extracted_text = pytesseract.image_to_string(image,lang=lancode)
        return jsonify({"detected_text": extracted_text})
    
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host ="0.0.0.0",debug=False,port=port)
