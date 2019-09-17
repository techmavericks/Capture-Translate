from flask import Flask,render_template,request,jsonify
from googletrans import Translator
translator = Translator()
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    text = request.json['key'][0]
    language = request.json['key'][1]
    a = translator.translate([text], dest=language)
    for i in a:
         translated_text= i.text
    return jsonify({"key" : translated_text})

if __name__ == "__main__":
    app.run(debug=True)
    