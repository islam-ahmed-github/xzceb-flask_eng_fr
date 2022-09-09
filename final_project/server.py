from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    return translator.Translate_en_to_fr(textToTranslate)
   

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    return translator.Translate_fr_to_en(textToTranslate)

@app.route("/")
def renderIndexPage():
    return "ibm-translation-server-by-islam-ahmed"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
