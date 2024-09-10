import os
from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Define the path to the CSV file
CSV_FILE_PATH = 'data.csv'

def clean_dataframe(df):
    """
    Cleans the dataframe by stripping whitespace from headers, dropping rows with missing values,
    and handling any extra spaces or hidden characters.
    """
    # Remove extra whitespace from column names
    df.columns = df.columns.str.strip()
    
    # Drop rows with all NaN values
    df.dropna(how='all', inplace=True)
    
    # Optionally, drop rows with any NaN values
    df.dropna(inplace=True)
    
    # Remove leading/trailing spaces from string data in the entire DataFrame
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    
    return df

def validate_excel_columns_and_types(excel_df, csv_df):
    """
    Validate that the columns and data types of the uploaded Excel file match the CSV file.
    
    Args:
    - excel_df: DataFrame of the uploaded Excel file.
    - csv_df: DataFrame of the existing CSV file.
    
    Returns:
    - (bool, str): A tuple containing a boolean indicating success and a feedback message.
    """
    feedback = []

    # Check if column names match
    if list(excel_df.columns) != list(csv_df.columns):
        feedback.append("Column names do not match.")
        feedback.append(f"Expected columns: {list(csv_df.columns)}")
        feedback.append(f"Found columns: {list(excel_df.columns)}")
        return False, "\n".join(feedback)

    # Check if column data types match
    for col in csv_df.columns:
        if excel_df[col].dtype != csv_df[col].dtype:
            feedback.append(f"Column '{col}' has incorrect data type.")
            feedback.append(f"Expected: {csv_df[col].dtype}, Found: {excel_df[col].dtype}")

    if feedback:
        return False, "\n".join(feedback)
    else:
        return True, "Validation successful."

def read_csv_file(file_path):
    """
    Reads a CSV file into a DataFrame, handling tokenization errors gracefully.
    
    Args:
    - file_path: Path to the CSV file.
    
    Returns:
    - DataFrame if successful, otherwise None.
    """
    try:
        # Try reading the CSV file with pandas, handling errors if they occur
        df = pd.read_csv(file_path, error_bad_lines=False, warn_bad_lines=True, delimiter=',', engine='python')
        return df
    except pd.errors.ParserError as e:
        print(f"Error parsing CSV file: {e}")
        return None

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
        try:
            # Read the uploaded Excel file into a DataFrame
            excel_df = pd.read_excel(file)
            
            # Clean the uploaded Excel DataFrame
            excel_df = clean_dataframe(excel_df)

            # Ensure the 'data' directory exists
            os.makedirs('data', exist_ok=True)

            # Read the existing CSV file
            csv_df = read_csv_file(CSV_FILE_PATH)
            if csv_df is None:
                return 'Error reading the CSV file to append to.'

            # Clean the CSV DataFrame
            csv_df = clean_dataframe(csv_df)

            # Validate the uploaded Excel file
            is_valid, feedback = validate_excel_columns_and_types(excel_df, csv_df)

            if is_valid:
                # Append the new data to the CSV
                excel_df.to_csv(CSV_FILE_PATH, mode='a', header=False, index=False)
                return 'File successfully uploaded, validated, and appended to CSV.'
            else:
                return f"File validation failed:\n{feedback}"
        except Exception as e:
            return f"An error occurred while processing the file: {e}"

    return 'File upload failed'

if __name__ == '__main__':
    app.run(debug=True)
