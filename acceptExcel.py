from flask import Flask, request, render_template
import pandas as pd
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')

def validate_data(df):
    # Check for empty cells
    if df.isnull().values.any():
        return 'The file contains empty cells. Please fill all required data.'

    # Data type validation
    if not pd.api.types.is_numeric_dtype(df['age']):
        return 'Invalid data type for age. It should be a number.'
    if not pd.api.types.is_numeric_dtype(df['balance']):
        return 'Invalid data type for balance. It should be a number.'
    if not pd.api.types.is_numeric_dtype(df['duration']):
        return 'Invalid data type for duration. It should be a number.'
    if not pd.api.types.is_numeric_dtype(df['campaign']):
        return 'Invalid data type for campaign. It should be a number.'
    if not pd.api.types.is_numeric_dtype(df['pdays']):
        return 'Invalid data type for pdays. It should be a number.'
    if not pd.api.types.is_numeric_dtype(df['previous']):
        return 'Invalid data type for previous. It should be a number.'

    # Range check for Age and Balance
    if not (df['age'].between(18, 100).all()):
        return 'Age should be between 18 and 100.'
    if not (df['balance'] >= 0).all():
        return 'Balance should be a non-negative value.'
    return 0

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

        # Validate the data
        validation_error = validate_data(df)
        if validation_error !=0:
            return validation_error

        # Run external validation script (if any)
        subprocess.run(["python", "validation.py"])

        # Append to CSV
        df.to_csv('data.csv', mode='a', sep=';', header=False, index=False)

        return 'File successfully uploaded and processed'
    return 'File upload failed'

if __name__ == '__main__':
    app.run(debug=True)
