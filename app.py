from flask import Flask, render_template, request
import pytesseract
from PIL import Image
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    text = ''
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            img = Image.open(filepath)
            text = pytesseract.image_to_string(img, lang='ben+eng')
            os.remove(filepath)

    return render_template('index.html', text=text)

if __name__ == '__main__':
    app.run(debug=True)
