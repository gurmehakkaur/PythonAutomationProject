from flask import Flask, request, render_template
import pandas as pd
import subprocess
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')  

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part in the request'
    file = request.files['file']
    if file.filename == '':
        return 'No file selected for uploading'
    if file:
        # Reading the file uploaded
        df = pd.read_excel(file)

        subprocess.run(["python", "validation.py"])

        df.to_csv('data.csv', mode='a', header=False, index=False)  

        return 'File successfully uploaded and processed'
    return 'File upload failed'

if __name__ == '__main__':
    app.run(debug=True)
