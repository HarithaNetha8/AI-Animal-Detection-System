from flask import Flask, render_template, request
import os
from detect import detect_animal

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    alert = False
    confidence = 0

    if request.method == 'POST':
        file = request.files['image']
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        alert, confidence = detect_animal(file_path)

    return render_template('index.html', alert=alert, confidence=confidence)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

