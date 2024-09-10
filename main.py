import subprocess
import sys

def main(auto_mode=False):
    # If the script is run in auto mode, skip the prompt and answer 'no' automatically
    if auto_mode:
        user_choice = 'n'
        print("Automatically answering 'no' for file upload.")
    else:
        # Asking user if they want to upload an Excel file (manual mode)
        user_choice = input("Do you want to add an Excel file? (y/n): ")

    if user_choice == 'y':
        # Opening Flask app to allow file upload, this script will also perform checks on the excel file first
        print("Opening the webpage to upload an Excel file...")
        subprocess.run(["python", "acceptExcel.py"])  # This will block execution until the Flask server is closed
    
    # Running validation script
    subprocess.run(["python", "validation.py"])

    # Running Data Representation script so that all the graphs get updated according to new data
    subprocess.run(["python", "dataRep.py"])

if __name__ == "__main__":
    # Check if the script is run in auto mode by passing an argument
    auto_mode = len(sys.argv) > 1 and sys.argv[1] == 'auto'
    main(auto_mode)


